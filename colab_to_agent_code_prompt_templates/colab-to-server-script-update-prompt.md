Update the existing Linux/server script `{SERVER_SCRIPT}` to match the new logic in `{NEW_COLAB_NOTEBOOK}`.

Do not recreate the script from scratch. 
Compare the new Colab notebook with the existing server script and modify the server script so it implements all new logic while preserving local Linux
execution, relative paths, Ollama integration, JSON handling, error handling, and standalone `main()` structure.

Remove all Colab-only code: Google Drive mounting, `/content/drive` paths, `!pip install`, shell notebook commands, `%magic`, and notebook UI logic.


# Apply these additional required changes:

- Remove the old `ONLY_APPLICANT = None` mechanism completely.
- Do not use single-applicant filtering.
- Add filtering through `FILTERED_LIST_Applicant_Application_ids.tsv`.
- The TSV file is located in the same directory as `doc_executiveSummary.py`.
- The TSV contains a column named `applicant_application`.
- Values in `applicant_application` correspond to subdirectory names under `dream_applicant_application/`.
- If the TSV exists, process only matching subdirectories.
- If the TSV does not exist, process all subdirectories.

