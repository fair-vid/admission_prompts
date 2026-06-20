# python3 doc_executiveSummary.py
#
# =============================================================================
# Document-Level Executive Summarization for International Admissions
# =============================================================================
#
# This script implements the document-level executive summarization stage
# of the AI-driven admissions evaluation pipeline.
#
# At this point in the workflow, individual document pages have already been:
#   - processed via OCR and vision-language models,
#   - reconstructed into coherent multi-page documents,
#   - stored as structured textual representations.
#
# The purpose of this stage is to elevate document processing from raw
# extraction to decision-oriented abstraction using a 2-stage process:
#   1. Initial Document Classification & General Extraction
#   2. Document-Specific Deep Dive Summarization
#
# Prerequisites:
#   - Ollama installed and running locally (https://ollama.com)
#   - The model pulled (e.g., ollama pull granite4.1:8b)
#   - Python packages: ollama, pandas
#
# =============================================================================

import json
import os
import re
import time
import subprocess
from pathlib import Path

import pandas as pd
import ollama

# =============================================================================
# Configuration
# =============================================================================

# Model selection
model_name = "granite4.1:8b"

# OCR model used in previous step
ocr_model_name = "glm-ocr"

# Input/Output directories
image_text_dir = f"documents_image_llm_text_{ocr_model_name}"
output_sub_dir_name = f"document_summaries___{ocr_model_name}_{re.sub(r'[^a-zA-Z0-9]', '', model_name)}"

# Base directory containing applicant subdirectories
base_dir = "dream_applicant_application/"

# TSV Filter file
filter_file = "FILTERED_LIST_Applicant_Application_ids.tsv"

# Prompts repository configuration
repo_url = "https://github.com/fair-vid/admission_prompts.git"
repo_dir = "admission_prompts"
prompt_folder = f"{repo_dir}/document_analysis"

# Error log directory
os.makedirs("tmp", exist_ok=True)


# =============================================================================
# Prompt Management
# =============================================================================

def setup_prompts_repo():
    if not os.path.exists(repo_dir):
        print("Cloning prompts repository...")
        subprocess.run(["git", "clone", repo_url, repo_dir], check=True)
    else:
        print("Updating prompts repository...")
        subprocess.run(["git", "-C", repo_dir, "pull"], check=True)

def load_prompts(directory_path):
    prompts = {}
    path = Path(directory_path)
    for file_path in path.glob("*.txt"):
        prompt_name = file_path.stem
        with open(file_path, 'r', encoding='utf-8') as f:
            prompts[prompt_name] = f.read()
    print(f"Loaded {len(prompts)} prompts.")
    return prompts

def get_classification_prompt(prompt_library, doc_text, file_name):
    prompt_template = prompt_library.get('document_classification_prompt')
    if not prompt_template:
        raise ValueError("document_classification_prompt not found in library")
    final_prompt = prompt_template.replace('{doc_text}', doc_text).replace('{file_name}', file_name)
    return final_prompt


# =============================================================================
# JSON Extraction Utility
# =============================================================================

def extract_json_from_response(response_text):
    """
    Extract and validate JSON from response text.
    Returns: (is_valid_json, content, file_extension)
    """
    json_pattern = r'```json\s*\n(.*?)\n```'
    match = re.search(json_pattern, response_text, re.DOTALL | re.IGNORECASE)

    if match:
        json_str = match.group(1).strip()
        try:
            json.loads(json_str)
            return True, json_str, '.json'
        except json.JSONDecodeError:
            return False, response_text, '.txt'

    try:
        json.loads(response_text)
        return True, response_text, '.json'
    except json.JSONDecodeError:
        return False, response_text, '.txt'


# =============================================================================
# Core Functions
# =============================================================================

def extract_with_ollama(prompt, model):
    try:
        response = ollama.generate(
            model=model,
            prompt=prompt,
            format='json'
        )
        return response["response"]
    except Exception as e:
        print(f"  Ollama error: {e}")
        try:
            with open("tmp/error_log.txt", "a", encoding='utf-8') as log_file:
                log_file.write(f"\n\n----------------\nmodel_name={model}\n\n  Error: {e}\n")
        except Exception:
            pass
        return None

def discover_subdirs(base_dir, filter_file):
    base_path = Path(base_dir)
    if not base_path.exists():
        print(f"ERROR: Base directory does not exist: {base_dir}")
        return []

    subdirs = []
    if os.path.exists(filter_file):
        print(f"Found filter file: {filter_file}")
        try:
            filter_df = pd.read_csv(filter_file, sep='\t')
            allowed_subdirs = set(filter_df['applicant_application'].astype(str).tolist())
            subdirs = [d.name for d in base_path.iterdir() if d.is_dir() and d.name in allowed_subdirs]
            print(f"Filtered to {len(subdirs)} subdirectories based on TSV.")
        except Exception as e:
            print(f"ERROR reading {filter_file}: {e}")
    else:
        print("No filter file found. Processing all subdirectories.")
        subdirs = [d.name for d in base_path.iterdir() if d.is_dir()]
    
    return subdirs

def get_files_by_subdir(base_dir, subdirs, image_text_dir):
    files_by_subdir = {}
    for subdir_name in subdirs:
        subdir = Path(base_dir) / subdir_name
        documents_text_path = subdir / image_text_dir
        if documents_text_path.exists() and documents_text_path.is_dir():
            files = sorted([f for f in documents_text_path.iterdir() if f.is_file()])
            files_by_subdir[subdir.name] = files
            print(f"Found {len(files)} files in {subdir.name}/{image_text_dir}/")
    return files_by_subdir


def process_stage_1(files_by_subdir, base_dir, model, output_sub_dir_name, prompt_library):
    total_processed = 0
    total_skipped = 0
    total_errors = 0
    
    for subdir_name, files in files_by_subdir.items():
        subdir_path = Path(base_dir) / subdir_name
        output_dir = subdir_path / output_sub_dir_name
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"\nProcessing {subdir_name} Stage 1 with {model}...")
        
        for i_file, text_file in enumerate(files):
            if (output_dir / f"{text_file.stem}.txt").exists() or \
               (output_dir / f"{text_file.stem}.json").exists():
                print(f"        ⊘ Skipped (already exists): {text_file.name}")
                total_skipped += 1
                continue
                
            try:
                doc_text = open(text_file, encoding='utf-8').read()
                prompt = get_classification_prompt(prompt_library, doc_text, text_file.name)
                
                print(f"\n {i_file}/{len(files)} {text_file.name} ")
                response_text = extract_with_ollama(prompt, model)
                
                if response_text is not None:
                    is_json, content, ext = extract_json_from_response(response_text)
                    output_file = output_dir / f"{text_file.stem}{ext}"
                    with open(output_file, 'w', encoding='utf-8') as f:
                        f.write(content)
                    total_processed += 1
                else:
                    print(f"  ✗ No response for {text_file.name}")
                    total_errors += 1
            except Exception as e:
                print(f"  ✗ Error processing {text_file.name}: {str(e)}")
                total_errors += 1
                
    return total_processed, total_skipped, total_errors


def process_stage_2(files_by_subdir, base_dir, model, output_sub_dir_name, prompt_library):
    for subdir_name, original_files in files_by_subdir.items():
        subdir_path = Path(base_dir) / subdir_name
        output_dir = subdir_path / output_sub_dir_name
        
        if not output_dir.exists():
            continue
            
        print(f"\nProcessing Stage 2 for {subdir_name}...")
        md_entries = []
        json_files = sorted(list(output_dir.glob("*.json")))
        
        for i_file, json_path in enumerate(json_files):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            except json.JSONDecodeError:
                print(f"           (Invalid JSON): {json_path.name}")
                continue
                
            if existing_data.get("_stage2_completed"):
                print(f"  ⊘ Skipped (Stage 2 already done): {json_path.name[:15]}...")
                formatted_json = json.dumps(existing_data, indent=4, ensure_ascii=False)
                md_entries.append(f"# {json_path.stem}\n```json\n{formatted_json}\n```\n")
                continue
                
            doc_type = existing_data.get("document_type", "")
            if not doc_type:
                print(f"  ⊘ Skipped (No document_type in JSON): {json_path.name[:15]}...")
                continue
                
            doc_type_clean = re.sub(r'[\s\-]+', '_', doc_type.lower().strip())
            country_code = existing_data.get("country_code", "")
            country_code_clean = country_code
            print(f"  Country Code: {country_code}")
            
            prompt_key = None
            if country_code_clean:
                country_specific_key = f"{country_code_clean}_{doc_type_clean}"
                country_specific_key_prompt = f"{country_code_clean}_{doc_type_clean}_prompt"
                if country_specific_key in prompt_library:
                    prompt_key = country_specific_key
                elif country_specific_key_prompt in prompt_library:
                    prompt_key = country_specific_key_prompt
                    
            if not prompt_key:
                if doc_type_clean in prompt_library:
                    prompt_key = doc_type_clean
                elif f"{doc_type_clean}_prompt" in prompt_library:
                    prompt_key = f"{doc_type_clean}_prompt"
                    
            if not prompt_key:
                print(f"  ⊘ Skipped (No exact prompt for '{doc_type}' or '{country_code}'): {json_path.name}...")
                continue
                
            original_file = next((f for f in original_files if f.stem == json_path.stem), None)
            if not original_file or not original_file.exists():
                print(f"  ⊘ Original text not found for {json_path.name}")
                continue
                
            original_doc_text = open(original_file, 'r', encoding='utf-8').read()
            prompt_template = prompt_library[prompt_key]
            final_prompt = prompt_template.replace('{doc_text}', original_doc_text)
            
            print(f"\n\n  → Running '{prompt_key}' for {json_path.name}... \n\n")
            
            response_text = extract_with_ollama(final_prompt, model)
            if response_text is not None:
                is_json, content, ext = extract_json_from_response(response_text)
                if is_json:
                    try:
                        new_data = json.loads(content)
                        existing_data["document_specific_details"] = new_data
                        existing_data["_stage2_completed"] = True
                        existing_data["_applied_prompt"] = prompt_key
                        
                        with open(json_path, 'w', encoding='utf-8') as f:
                            json.dump(existing_data, f, indent=4, ensure_ascii=False)
                            
                        print("✅ Appended & Saved")
                        formatted_json = json.dumps(existing_data, indent=4, ensure_ascii=False)
                        md_entries.append(f"# {json_path.stem}\n```json\n{formatted_json}\n```\n")
                    except json.JSONDecodeError:
                        print("❌ Failed (Invalid JSON generated in Stage 2)")
                else:
                    print("❌ Failed (No JSON found in Stage 2 output)")
            else:
                print("❌ Failed (Ollama error)")
                
        if md_entries:
            md_file_path = subdir_path / f"{output_sub_dir_name}_combined_stage2_results.md"
            with open(md_file_path, 'w', encoding='utf-8') as md_file:
                md_file.write(f"# All Summaries for Applicant: {subdir_name}\n\n")
                md_file.write("\n---\n\n".join(md_entries))
            print(f"\n📄 Saved combined Markdown file to: {md_file_path}")

# =============================================================================
# Main Entry Point
# =============================================================================

def process_all_applicants():
    print("=" * 60)
    print("Document-Level Executive Summarization (2 Stages)")
    print(f"  Model:          {model_name}")
    print(f"  Base dir:       {base_dir}")
    print(f"  Input dir:      {image_text_dir}")
    print(f"  Output dir:     {output_sub_dir_name}")
    print("=" * 60)

    if not os.path.isdir(base_dir):
        print(f"\nERROR: Base directory not found: {base_dir}")
        print("Please ensure dream_applicant_application/ exists in the current directory,")
        print("or update the 'base_dir' variable at the top of this script.")
        exit(1)
        
    setup_prompts_repo()
    prompt_library = load_prompts(prompt_folder)
    
    subdirs = discover_subdirs(base_dir, filter_file)
    if not subdirs:
        print("No subdirectories to process. Exiting.")
        return
        
    files_by_subdir = get_files_by_subdir(base_dir, subdirs, image_text_dir)
    if not files_by_subdir:
        print("No files found in the discovered subdirectories. Exiting.")
        return
        
    print("\n--- Starting Stage 1 ---")
    start_time = time.time()
    process_stage_1(files_by_subdir, base_dir, model_name, output_sub_dir_name, prompt_library)
    
    print("\n--- Starting Stage 2 ---")
    process_stage_2(files_by_subdir, base_dir, model_name, output_sub_dir_name, prompt_library)
    
    print("\n" + "=" * 60)
    print("All documents processed!")
    print(f"  Total time: {time.time() - start_time:.2f}s")
    print("=" * 60)

if __name__ == "__main__":
    process_all_applicants()
