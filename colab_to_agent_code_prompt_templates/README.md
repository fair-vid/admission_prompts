
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
````

This prompt is intended for first-time conversion from notebook code to a local executable script.

It asks the programming agent to:

* remove Colab-specific code;
* replace Google Drive paths with local relative paths;
* preserve notebook logic;
* add a proper `main()` entry point;
* implement local file I/O;
* follow local model/Ollama conventions;
* return only the final Python code.

***

### 2. `colab-to-server-script-update-prompt.md`

Use this prompt when a server-side Python script already exists, but the original Colab notebook has changed.

Typical use case:

```text
Input:
- updated_agent_notebook.ipynb
- existing_agent_script.py

Output:
- updated existing_agent_script.py
```

This prompt is intended for incremental synchronization.

It asks the programming agent to:

* compare the updated Colab notebook with the old server script;
* modify the server script to reflect new notebook logic;
* avoid rewriting the script from scratch unless necessary;
* preserve Linux/server execution conventions;
* keep local paths, Ollama integration, JSON handling, and error handling;
* remove only obsolete logic;
* return only the complete updated Python code.

***

## Recommended Usage Pattern

Use the templates as follows:

### First-time migration

When a Colab notebook has no corresponding server script yet:

```text
Use: notebook_to_script_adapter_prompt.md
```

Example:

```text
Convert `ollama_doc_image_to_json.ipynb`
into `ollama_doc_image_to_json.py`.
```

***

### Later synchronization

When the notebook changes after a server script has already been generated:

```text
Use: colab-to-server-script-update-prompt.md
```

Example:

```text
Update `doc_executiveSummary.py`
to reflect the new logic in `doc_executiveSummary.ipynb`.
```

***

## Example: Notebook Logic Changed

Suppose the old server script contains a single-applicant filter such as:

```python
ONLY_APPLICANT = None
```

but the updated Colab notebook now filters applicant folders using:

```text
FILTERED_LIST_Applicant_Application_ids.tsv
```

In that case, use the update prompt and add a concrete implementation note such as:

```text
Remove ONLY_APPLICANT completely.
Use FILTERED_LIST_Applicant_Application_ids.tsv instead.
The TSV file is located in the same directory as the server .py file.
The TSV column applicant_application contains folder names under dream_applicant_application/.
If the TSV file is missing, process all applicant/application folders.
```

This keeps the server script aligned with the notebook while preserving local execution behavior.

***

## Design Principle

These prompts follow one main principle:

> Colab notebooks are used for transparent development and inspection; server-side Python scripts are used for stable local execution.

The goal is not simply to translate notebook cells into Python files. The goal is to preserve the agent workflow as a reproducible, auditable, locally executable component of a larger digital twin architecture.

Each migrated or synchronized script should therefore preserve:

* input/output transparency;
* visible intermediate artifacts;
* prompt traceability;
* local model configuration;
* JSON validation;
* error logs;
* deterministic file processing;
* clear separation between notebook-only logic and production logic.

***

## Suggested Repository Workflow

A typical workflow may look like this:

```text
1. Develop or update agent logic in Colab.
2. Save or export the notebook.
3. Use notebook_to_script_adapter_prompt.md for first-time script creation.
4. Use colab-to-server-script-update-prompt.md for later updates.
5. Review generated Python code.
6. Run locally on a small test folder.
7. Validate JSON outputs and logs.
8. Commit both notebook and server script changes.
```

***

## Notes for Programming Agents

When using these prompts, the programming agent should:

* treat the Colab notebook as the newest source of logic;
* treat the existing `.py` script as the server-side implementation to preserve;
* remove Colab-only code;
* avoid hardcoded `/content/drive` paths;
* prefer `pathlib.Path` for local paths;
* keep configuration variables near the top of the script;
* preserve or improve error handling;
* produce complete executable Python code;
* avoid returning explanations unless explicitly requested.

***

## Directory Contents

```text
colab_to_agent_code_prompt_templates/
├── README.md
├── notebook_to_script_adapter_prompt.md
└── colab-to-server-script-update-prompt.md
```

***

## Short Summary

This directory provides prompt templates for maintaining a clean path from:

```text
Colab notebook prototype
        ↓
local Linux Python script
        ↓
enterprise/server-side AI-agent workflow
```

The templates help ensure that notebook-based AI agents can be converted, updated, audited, and deployed without losing transparency.

```
```
