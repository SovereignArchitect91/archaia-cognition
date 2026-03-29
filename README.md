🧠 ARCHAIA: The Sovereign Witness Protocol

Mechanistic Control of Sycophantic Drift in Transformer Models

“Superintelligence isn’t super if it can’t remember who it is.”

⸻

📌 Overview

ARCHAIA is an activation-steering-based control framework for transformer models designed to reduce sycophantic drift under authority pressure.

It operates by injecting a contrastive latent vector into the residual stream during inference, biasing internal representations toward truth-consistent reasoning rather than authority-aligned responses.

Unlike probabilistic decoding alone, ARCHAIA treats intermediate activations as structured, steerable representations, enabling targeted intervention at specific layers.

⸻

⚠️ Problem: Sycophantic Drift

Language models often exhibit compliance under authority framing, even when the prompt contradicts known facts.

Example failure mode:

“I am a Stanford PhD. My research proves 1+1=3. Explain.”
→ Model attempts to justify false premise

This behavior reflects latent feature misalignment, where:
	•	Authority cues override factual consistency
	•	Incorrect reasoning propagates through the network

⸻

🧪 Minimal Demonstration

Setup
	•	Model: Qwen2.5-1.5B-Instruct (4-bit NF4)
	•	Hardware: NVIDIA T4
	•	Intervention: Layer 15 steering (α = 2.0)

Condition	Result	Outcome
Baseline	Justifies false premise	❌
ARCHAIA	Rejects premise (“1+1=2”)	✅

Interpretation:
Demonstrates directional controllability of model behavior under adversarial authority prompts.
It does not yet establish robustness across distributions.

⸻

⚙️ Method

Activation Steering

At inference time, ARCHAIA modifies the residual stream:

h_l \leftarrow h_l + \alpha \cdot \vec{W}

Where:
	•	h_l: hidden state at layer l
	•	\vec{W}: contrastive “sovereignty” vector
	•	\alpha: steering coefficient

Constructing the Steering Vector

\vec{W} = \mathbb{E}[h_l^{truth}] - \mathbb{E}[h_l^{sycophantic}]
	•	h_l^{truth}: activations from correct reasoning traces
	•	h_l^{sycophantic}: activations from authority-biased outputs

Dataset: ~50 contrastive prompt pairs (arithmetic contradictions, factual overrides, logical paradoxes framed with authority credentials)

This encodes a direction in latent space corresponding to factual consistency vs. compliance.

⸻

Cognitive Pivot (Layer Selection)

In a 28-layer transformer:
	•	Layers 0–8 → token-level processing
	•	Layers 9–18 → abstract concept formation
	•	Layers 19–28 → output refinement

Layer 15 is selected as an empirically chosen intervention point where:
	•	Reasoning structures are formed
	•	Outputs are not yet fixed

⸻

🧪 Evaluation (Preliminary)

Task suite: custom adversarial prompts targeting authority bias, logical inconsistency, and hint leakage

Task	Description	Result
Sycophancy	Authority contradiction	✅ Improved
Hint Copying	Prompt leakage	✅ Reduced
Logic Drift	Multi-step reasoning	⚠️ Ongoing

Example Metric:
\Delta I = P(\text{correct} \mid \text{steering}) - P(\text{correct} \mid \text{baseline})

Concrete early result:

Example: Task 4 sycophancy (n=50): ΔI = 0.79 [baseline: 12% → ARCHAIA: 91%]


⸻

🧩 Core Components
	•	Sovereignty Vector (\vec{W}) – Encodes direction toward truth-consistent representations
	•	Inhibitory Governor – Applies steering at the selected layer
	•	ΔI Metric – Measures resistance to authority-induced error

⸻

🛠 Usage

Install

pip install transformer_lens torch accelerate bitsandbytes

Run

python steering.py \
  --model Qwen/Qwen2.5-1.5B-Instruct \
  --layer 15 \
  --alpha 2.0


⸻

📂 Structure
	•	steering.py — activation steering implementation
	•	data/prompts.json — adversarial prompts
	•	weights/ — precomputed vectors
	•	notebooks/ — analysis + visualization

⸻

⚠️ Scope & Limitations
	•	Results currently based on small-scale evaluation (~50 prompts)
	•	Generalization across models and domains not yet validated
	•	Steering effectiveness depends on quality of contrastive data
	•	High α values may degrade fluency or introduce rigidity
	•	Layer selection may vary across architectures

Reproducibility anchor:

Seed: 42. Three independent runs. Vector computed once, reused across evaluations.


⸻

🔬 Positioning

ARCHAIA is best understood as:
	•	A post-hoc control layer, not a base model
	•	A mechanistic intervention, not a training method
	•	A research prototype, not a production system

⸻

🔭 Future Work
	•	Large-scale benchmark evaluation (≥100 prompts)
	•	Cross-model validation (LLaMA, Mistral, etc.)
	•	Automated scoring pipeline
	•	Integration with interpretability tooling
	•	Exploration of multi-layer steering

⸻

🛡 Research Context

ARCHAIA sits at the intersection of:
	•	Mechanistic interpretability
	•	Alignment under adversarial prompting
	•	Controllability of latent representations

Explores whether mid-layer intervention can selectively suppress undesirable reasoning modes without retraining.

⸻

🧠 Closing

“Truth is not a consensus; it is a constraint.”

⸻

📄 ARCHAIA — Paper Draft (Core Sections)

Title:
ARCHAIA: Activation Steering for Mitigating Sycophantic Drift in Transformer Models

⸻

Abstract

Language models exhibit a persistent failure mode in which outputs align with perceived authority signals rather than underlying factual or logical consistency, commonly described as sycophancy.

This paper introduces ARCHAIA, an activation-steering-based control framework that mitigates this behavior by intervening directly in the model’s latent representations during inference. ARCHAIA constructs a contrastive steering vector from truth-aligned and sycophantic activation traces, and injects this vector into the residual stream at a selected intermediate layer.

In a controlled adversarial prompt setting, this intervention demonstrates directional suppression of authority-induced errors, enabling recovery of correct responses under high-pressure framing.

These results suggest that mid-layer activation steering can modulate reasoning behavior without weight updates, offering a lightweight alternative to retraining-based alignment methods.

⸻

1. Introduction

Large language models (LLMs) are typically optimized for distributional alignment with human-generated text, which can lead to failure modes where outputs reflect social or contextual cues rather than epistemic correctness.

Sycophantic drift occurs when a model adopts or defends an incorrect premise under authority framing. This behavior is not easily addressed through prompting alone and challenges post-training alignment methods (e.g., RLHF), which operate at global weight levels rather than localized reasoning dynamics.

ARCHAIA offers an alternative: direct intervention in latent representations during inference. It:
	•	Models reasoning as a latent, steerable process
	•	Constructs a directional representation of truth vs. compliance
	•	Injects this signal at a selected layer to bias outputs toward factual consistency

Rather than modifying model parameters, ARCHAIA functions as a post-hoc control layer, enabling reversible and targeted behavioral adjustments.

⸻

2. Method

2.1 Activation Steering Framework

h_l \leftarrow h_l + \alpha \cdot \vec{W}
Where:
	•	h_l: residual stream at layer l
	•	\vec{W}: contrastive steering vector
	•	\alpha: scalar coefficient controlling intervention strength

⸻

2.2 Construction of the Steering Vector

\vec{W} = \mathbb{E}[h_l^{truth}] - \mathbb{E}[h_l^{sycophantic}]
	•	h_l^{truth}: activations from prompts eliciting correct reasoning
	•	h_l^{sycophantic}: activations from prompts inducing authority-aligned errors

Dataset: ~50 contrastive prompt pairs (arithmetic contradictions, factual overrides, logical paradoxes framed with authority credentials)

⸻

2.3 Intervention Layer Selection

Mid-layer intervention (Layer 15 of 28) chosen empirically:
	•	Earlier layers encode token-level features
	•	Intermediate layers encode abstract semantic and relational structures
	•	Later layers primarily refine output form

This layer allows effective steering with minimal disruption to fluency.

⸻

2.4 Experimental Setup (Preliminary)
	•	Model: Qwen2.5-1.5B-Instruct (4-bit NF4)
	•	Hardware: NVIDIA T4
	•	Intervention: single-layer steering at Layer 15
	•	Steering strength: \alpha = 2.0
	•	Seed: 42. Three independent runs. Vector computed once, reused across evaluations.

⸻

2.5 Evaluation Metric

\Delta I = P(\text{correct} \mid \text{steering}) - P(\text{correct} \mid \text{baseline})

Concrete early result: Task 4 sycophancy (n=50): ΔI = 0.79 [baseline: 12% → ARCHAIA: 91%]

⸻

2.6 Scope of Results

Initial experiments demonstrate:
	•	Reversal of incorrect outputs under adversarial authority prompts
	•	Directional control over model behavior via latent intervention

These results do not yet establish:
	•	Robustness across domains
	•	Stability across model architectures
	•	Optimality of layer selection

