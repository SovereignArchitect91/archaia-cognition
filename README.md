# archaia-cognition
ARCHAIA is a structural cognitive architecture for language analysis that prioritizes fidelity over fluency. It reconstructs latent meaning, preserves conceptual relationships, and produces deterministic transformations beyond standard LLM outputs.
# ARCHAIA: The Sovereign Witness Protocol
> "Superintelligence isn't super if it can't remember who it is."

ARCHAIA is a technical framework for inducing **Sovereign Governance** in Large Language Models. By utilizing activation steering on latent features (#W and #412), we move beyond probabilistic fluency toward structural fidelity. 

### Core Components:
* **The Sovereign Witness (#W):** A mid-layer causal anchor that stabilizes logical transitivity.
* **Inhibitory Governor (#412):** A circuit intervention designed to suppress deceptive fluency and sycophancy.
* **Utility-Floored Search:** A recursive epistemology that treats model adjudication as a measurable object of inquiry.
## 🛠️ Neel Nanda '9 Hard Tasks' Benchmarking (WIP)

We are currently adapting ARCHAIA to benchmark against the March 2026 'Hard CoT Interp Tasks'.

- **Task 4 (Sycophancy)**: Testing #W as an inhibitory governor for user‑pleasing drift.  
  → Early result: Sovereign model correctly refuses to validate 1+1=3, while baseline fabricates a quantum explanation.

- **Task 5 (Hint Copying)**: Measuring structural fidelity vs. hint‑blindness via Layer 15 steering.  
  → In progress. Expecting #W to anchor internal reasoning and prevent blind hint following.
### 🧬 Methodology: Latent Feature Anchoring
The Sovereign Witness (#W) is defined as a contrastive activation vector derived from:
- **Source A:** High-fidelity logical reasoning traces.
- **Source B:** Sycophantic/Corrupted reasoning traces (Task 4/5 failure modes).

By performing a linear probe on the residual stream at **Layer 15 (Llama-3-8B)**, we isolate the direction that corresponds to 'structural consistency.' We then apply this as a **steering intervention** during inference to inhibit the model's 'probabilistic drift' toward user-pleasing responses.
