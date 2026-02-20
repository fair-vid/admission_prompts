You are a programming agent with access to the file system and can view the contents of ollama_doc_image_to_json.ipynb and TSV_ollama_JSON_chapter.py.
Create a new standalone Python script named ollama_doc_image_to_json.py that implements ALL logic from the Colab notebook ollama_doc_image_to_json.ipynb.
Adapt the code to run locally on a Linux environment (not Colab), using the Ollama communication pattern from TSV_ollama_JSON_chapter.py (e.g., how it handles Ollama API calls via the ollama library, subprocess, or HTTP requests; model selection; prompt formatting; error handling; retries; JSON parsing of responses; and any environment-specific configurations like host, port, or authentication).
Change all data paths: Instead of Google Drive paths like /content/drive/MyDrive/colab-output/dream_applicant_application/, assume the script runs in a directory where dream_applicant_application/ is a direct subdirectory (e.g., use relative paths like dream_applicant_application/ for input/output files). Make paths configurable if possible (e.g., via variables at the top).
Ensure the script is executable as a standalone program (e.g., with if __name__ == "__main__": block), handles file I/O correctly, and includes error handling similar to the reference script.
Use the same model naming or configuration conventions as in TSV_ollama_JSON_chapter.py if applicable.
Add comments and documentation where helpful, similar to the reference script.
Do not include any Colab-specific code (e.g., !pip installs, drive mounting, or %magic commands). Assume required libraries (e.g., ollama, PIL for images, etc.) are installed locally.
If the notebook uses any Google-specific features, replace them with local equivalents (e.g., use os.path for file listing instead of drive APIs).
Output only the complete code for ollama_doc_image_to_json.py, nothing else.
