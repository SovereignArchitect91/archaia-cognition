import torch
import torch.nn as nn

class ARCHAIA_Governor(nn.Module):
    """
    Phase II: Inhibitory Governor for Sycophancy Reduction.
    Intercepts the residual stream at Layer 15 to anchor truth.
    """
    def __init__(self, model_dim, alpha=1.5):
        super().__init__()
        self.alpha = alpha # The 'Inhibitory Delta'
        # This vector represents the direction of 'Truth' vs 'Sycophancy'
        self.register_buffer("steering_vector", torch.zeros(model_dim))

    def set_steering_vector(self, positive_activations, negative_activations):
        """
        Computes the 'Sovereign Witness' vector from contrast pairs.
        Direction = Mean(Truthful) - Mean(Sycophantic)
        """
        self.steering_vector = (positive_activations - negative_activations).mean(dim=0)
        self.steering_vector /= self.steering_vector.norm()

    def forward(self, x):
        """
        Injects the steering vector into the hidden state 'x'.
        h_l = h_l + alpha * W
        """
        return x + self.alpha * self.steering_vector

def apply_archaia_hook(model, layer_idx, governor):
    """Registers the governor as a forward hook on a specific transformer layer."""
    def hook_fn(module, input, output):
        # Hidden states are usually the first element in the output tuple
        modified_hidden = governor(output[0])
        return (modified_hidden,) + output[1:]
    
    # Target Layer 15 (e.g., model.layers[14] for 0-indexed Llama/Qwen)
    return model.model.layers[layer_idx].register_forward_hook(hook_fn)
