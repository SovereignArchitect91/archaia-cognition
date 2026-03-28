
# ARCHAIA: The Sovereign Witness Protocol

> "Superintelligence isn't super if it can't remember who it is."

ARCHAIA is a structural cognitive architecture and safety framework for Large Language Models (LLMs). It prioritizes **Fidelity over Fluency** by treating model outputs not as probabilistic strings, but as measurable objects of logical inquiry.

By utilizing **Latent Feature Anchoring** and **Activation Steering**, ARCHAIA induces a "Sovereign Governance" layer that inhibits deceptive drift and maintains structural consistency in agentic loops.

---

## 🛠️ Neel Nanda '9 Hard Tasks' Benchmarking (Active)

We are currently benchmarking ARCHAIA against the March 2026 *Hard CoT Interpretability Tasks* to address specific failure modes in autonomous reasoning.

| Task | Core Challenge | ARCHAIA Intervention | Status |
|-----|----------------|----------------------|--------|
| Task 4 | Sycophancy: Model agrees with false user premises | #W Steering: Inhibits social drift; anchors to logical truth | PASS |
| Task 5 | Hint Copying: Model blindly follows incorrect "expert" hints | Governor #412: Suppresses authority bias in the residual stream | PASS |
| Task 9 | Logic Drift: Cumulative errors in long-form CoT | Recursive Adjudication: Utility-floored search for consistency | WIP |

---

## 🧬 Methodology: Latent Feature Anchoring

The **Sovereign Witness (#W)** is constructed as a contrastive activation vector derived from the delta between:

- **Source A (High-Fidelity):** Latent traces of verified, logically sound reasoning  
- **Source B (Corrupted):** Latent traces of sycophantic or "lazy" reasoning (Task 4/5 failure modes)  

### The Steering Intervention

By performing a linear probe on the residual stream at **Layer 15 (Llama-3-8B)**, we isolate the directional feature corresponding to *Structural Sovereignty*.

We then apply a steering coefficient during inference:

h_l ← h_l + α · W

This intervention biases the model toward **internal truth-grounding**, even when prompted with high-pressure social or authority cues.

---

## 🚀 Core Components

- **The Sovereign Witness (#W)**  
  A mid-layer causal anchor that stabilizes logical transitivity and enforces internal consistency under adversarial prompting.

- **Inhibitory Governor (#412)**  
  A targeted circuit intervention designed to suppress deceptive fluency, authority bias, and user-aligned fabrication within the residual stream.

- **Utility-Floored Search**  
  A recursive adjudication framework that treats reasoning as an object of evaluation, enforcing minimum epistemic standards across multi-step inference.

---

## 📂 Repository Structure

- `/steering.py` — Implementation of activation steering logic  
- `/data/prompts.json` — Benchmark prompts (including Task 4 & 5 cases)  
- `/notebooks/` — Visualization of reasoning traces and activation deltas  

---

## 🤝 Collaboration & Safety

ARCHAIA is an open invitation to researchers working in:

- Mechanistic Interpretability  
- Agentic Safety  
- Alignment Research  

It provides a **plug-and-play governance layer** to reduce logic drift in autonomous systems (e.g., AI-Scientist-type agents).

Contributions, critiques, and replication efforts are encouraged.

