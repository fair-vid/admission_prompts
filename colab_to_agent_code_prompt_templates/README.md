# Colab-to-Agent Code Prompt Templates

This directory contains reusable prompt templates for converting and synchronizing Google Colab notebook logic with local Linux/server-side Python scripts.

The purpose of these prompts is to support the **Colab-to-Enterprise Digital Twin Pattern**: first develop AI-agent workflow logic in transparent, inspectable Colab notebooks, then migrate or synchronize that logic into local/server-side Python programs while preserving reproducibility, auditability, and modular agent structure.

In this workflow, Colab notebooks act as the experimental and transparent source layer, while server-side Python scripts act as the production-oriented execution layer.

---

## Why These Prompts Exist

AI-agent pipelines often start in notebooks because notebooks are easy to inspect, run step by step, and share with students, researchers, administrators, or auditors.

However, production or institutional deployment usually requires standalone Python scripts that can run locally on Linux servers, use relative paths, call local models through Ollama, and avoid Colab-specific dependencies such as Google Drive mounting or notebook shell commands.

These prompt templates help a programming agent perform that migration consistently.

They are designed for workflows where:

- Colab notebooks define the newest agent logic;
- server-side `.py` files implement that logic in a local Linux environment;
- local file structures replace Google Drive paths;
- Ollama or other local model runtimes replace notebook-specific execution assumptions;
- intermediate files, JSON outputs, prompts, and logs remain inspectable;
- code changes preserve transparency and auditability.

---

## Current Prompt Templates

### 1. `notebook_to_script_adapter_prompt.md`

Use this prompt when creating a **new standalone Linux Python script** from an existing Colab notebook.

Typical use case:

```text
Input:
- some_agent_notebook.ipynb

Output:
- some_agent_script.py
