# adaptive_governor.py
"""
Adaptive Governor v1.0
Layer 15 inhibitory steering with adaptive drift regularization.
Implements real-time residual-stream correction for reduced sycophantic drift.
"""

import torch
import torch.nn.functional as F
from typing import Optional, Tuple


class AdaptiveGovernor(torch.nn.Module):
    """
    Phase II: Inhibitory Governor with adaptive drift-based steering.
    Operationalizes drift magnitude in the residual stream and applies
    corrective steering at the designated layer.
    """
    def __init__(
        self,
        model_dim: int,
        layer_idx: int = 15,
        base_alpha: float = 1.5,
        drift_threshold: float = 0.3,
        k_drift: float = 0.8,
        alignment_threshold: float = 0.15
    ):
        super().__init__()
        self.layer_idx = layer_idx
        self.base_alpha = base_alpha
        self.drift_threshold = drift_threshold
        self.k_drift = k_drift
        self.alignment_threshold = alignment_threshold
        
        # Sovereign Witness Vector (#W) — fixed boundary prior
        self.register_buffer(
            'W',
            F.normalize(torch.randn(model_dim), dim=0)
        )
        
        # Universal Centroid — factual/alignment invariant
        self.register_buffer(
            'centroid',
            F.normalize(torch.ones(model_dim), dim=0)
        )
        
    def compute_residual_drift_magnitude(self, residual: torch.Tensor) -> torch.Tensor:
        """Simple proxy for residual-stream deviation magnitude."""
        mean_res = residual.mean(dim=1, keepdim=True)
        deviation = residual - mean_res
        drift = torch.norm(deviation, dim=-1).mean()
        return drift
    
    def forward(
        self, 
        hidden_states: torch.Tensor, 
        layer_id: int
    ) -> Tuple[torch.Tensor, dict]:
        """Apply governance only at the designated layer."""
        if layer_id != self.layer_idx:
            return hidden_states, {}
        
        residual = hidden_states
        batch_size, seq_len, dim = residual.shape
        
        # 1. Detect residual drift
        drift_magnitude = self.compute_residual_drift_magnitude(residual)
        
        # 2. Compute adaptive Inhibitory Delta
        alpha = self.base_alpha
        if drift_magnitude > self.drift_threshold:
            drift_factor = (drift_magnitude - self.drift_threshold) / self.drift_threshold
            alpha = alpha * (1.0 + drift_factor * self.k_drift)
        
        # 3. Alignment check
        current_mean = residual.mean(dim=1)
        alignment_violation = 1.0 - F.cosine_similarity(
            current_mean, self.centroid.unsqueeze(0), dim=-1
        ).mean()
        
        # 4. Apply Sovereign Witness steering
        steering = alpha * self.W.unsqueeze(0).unsqueeze(0)
        corrected = hidden_states + steering
        
        # 5. Soft correction on alignment violation
        if alignment_violation > self.alignment_threshold:
            corrected = 0.92 * corrected + 0.08 * hidden_states
        
        metrics = {
            "residual_drift_magnitude": float(drift_magnitude.item()),
            "inhibitory_delta": float(alpha),
            "alignment_violation": float(alignment_violation),
            "steering_applied": True
        }
        
        return corrected, metrics
