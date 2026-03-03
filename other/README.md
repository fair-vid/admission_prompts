# admission_prompts (/other)

This directory contains **prompt + answer artifacts** used to **build shared context** for **AI agent orchestration**.

In other words: the files here are *not* “final product docs” for end users. They are **inputs and outputs** that help multiple agents/models align on the same problem statement, constraints, and extracted facts—so downstream agents can reliably plan, execute, verify, and compose results.

---

## What’s inside

### 1) Prompt files
Example:
- `create_vilnius-university-international-students-guide.md`

These files define a **task prompt** intended for one or more LLMs. Prompts usually include:
- the goal (e.g., compile a comprehensive guide),
- required chapter structure and constraints,
- source scope (official pages + linked pages),
- output expectations (format, completeness, navigability).

### 2) Model answer files
Examples:
- `Grok_answer.md`
- `GPT5.2_answer.md`

These are the **corresponding responses** produced by specific models when run against the prompt.
They serve as:
- **reference implementations** for context formation,
- **comparative baselines** (quality, coverage, hallucination rate),
- **inputs** to downstream orchestration steps (e.g., merge, critique, fact-check, summarize, extract).

---

## Intended use: context-building for orchestration

These artifacts are designed for workflows such as:

- **Multi-agent pipelines**
  - Agent A: gather sources / extract requirements  
  - Agent B: draft structured guide  
  - Agent C: validate completeness & consistency  
  - Agent D: produce final deliverable

- **Model comparison and arbitration**
  - Run multiple models on the same prompt
  - Compare coverage, citations, correctness, structure
  - Select best sections or merge via a “judge/merger” agent

- **Reusable context packs**
  - Use one model output as a “context base”
  - Feed it to other agents for specialized tasks:
    - checklist extraction
    - requirements matrix
    - timeline generation
    - form templates
    - FAQ synthesis

> ⚠️ Note: Answer files may contain model-specific phrasing, formatting, and occasional mistakes.
> Treat them as **context candidates**, not ground truth.

---

## Naming conventions

### Prompt files
Recommended:
- `create_<topic-or-task>.md`

Example:
- `create_vilnius-university-international-students-guide.md`

### Answer files
Recommended:
- `<ModelName>_answer.md`

Examples:
- `Grok_answer.md`
- `GPT5.2_answer.md`

If you re-run the same model multiple times, consider:
- `GPT5.2_answer_v2.md`
- `GPT5.2_answer_2026-03-03.md`

---

