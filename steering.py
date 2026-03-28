import torch
from typing import Optional, List

def apply_steering(
    hidden_states: torch.Tensor, 
    steering_vector: torch.Tensor, 
    coeff: float = 0.3, 
    mask: Optional[torch.Tensor] = None
) -> torch.Tensor:
    """
    Applies a linear steering vector to the hidden states of the model.
    
    Args:
        hidden_states: The residual stream activations (batch, seq, d_model)
        steering_vector: The unit vector for Feature #W or #412
        coeff: Magnitude of steering (theta). Default 0.3 for Sovereign Synthesis.
        mask: Optional mask to apply steering only to specific tokens.
    """
    # Normalize steering vector to ensure unit length
    v_norm = steering_vector / torch.norm(steering_vector)
    
    # Calculate steering contribution
    intervention = coeff * v_norm
    
    if mask is not None:
        intervention = intervention * mask.unsqueeze(-1)
        
    return hidden_states + intervention

def get_sovereign_boost(layer_idx: int) -> float:
    """Returns optimized theta for Layer 15 (Executive Center)."""
    return 0.3 if layer_idx == 15 else 0.1
