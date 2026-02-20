
# Agent Task: Convert Colab Notebook to Local Python Script

## Goal

Create a new standalone Python script named **`ollama_doc_image_to_json.py`** that fully reimplements the logic from a Colab notebook, adapted for a local Linux environment.

---

## Source Files

| File | Role |
|------|------|
| `ollama_doc_image_to_json.ipynb` | Colab notebook containing the original logic to migrate |
| `TSV_ollama_JSON_chapter.py` | Reference script providing the Ollama communication pattern to follow |

---

## Requirements

### 1. Implement All Notebook Logic
Replicate **all** logic from `ollama_doc_image_to_json.ipynb` in the new script — no functionality should be omitted.

### 2. Adapt for Local Linux (not Colab)
Follow the Ollama integration pattern from `TSV_ollama_JSON_chapter.py`, including:
- Ollama API calls (via `ollama` library, subprocess, or HTTP requests)
- Model selection
- Prompt formatting
- Error handling and retries
- JSON parsing of responses
- Environment-specific configuration (host, port, authentication)

### 3. Update Data Paths
- **Remove** all Google Drive paths (e.g., `/content/drive/MyDrive/colab-output/dream_applicant_application/`)
- **Use relative paths** instead, assuming the script runs in a directory where `dream_applicant_application/` is a direct subdirectory:
  ```
  dream_applicant_application/   ← input/output files live here
  ```
- Make paths **configurable via variables** at the top of the script where possible.

### 4. Standalone Executable Script
- Include an `if __name__ == "__main__":` block
- Handle file I/O correctly
- Include error handling consistent with the reference script

### 5. Model Naming & Configuration
Use the same model naming/configuration conventions as in `TSV_ollama_JSON_chapter.py`.

### 6. Comments & Documentation
Add comments and docstrings where helpful, following the style of the reference script.

---

## Constraints

- ❌ No Colab-specific code:
  - No `!pip install` commands
  - No Google Drive mounting
  - No `%magic` commands
- ✅ Assume all required libraries are already installed locally (e.g., `ollama`, `PIL`, etc.)
- Replace any Google-specific APIs with local equivalents (e.g., use `os.path` for file listing)

---

## Output

Return **only** the complete code for `ollama_doc_image_to_json.py` — nothing else.






