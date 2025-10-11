# admission_prompts


# FAIR-VID Prompts Repository

Publicly available prompts for interacting with Large Language Models (LLMs) during various stages of the **admission process**. These prompts are designed to support **communication**, **evaluation**, and **fraud detection** in a fair, transparent, and auditable manner.

---

## 📌 Overview
This repository is part of the [FAIR-VID Project](https://github.com/fair-vid), which introduces a **multimodal pre-processing pipeline** for applicant video interviews, documents, and form data. The goal is to enable **human–AI collaboration** in admissions and recruitment workflows by providing **open-source tools and prompts** for:

- 🎥 Video Interview Analysis  
- 📄 Document Understanding & Credential Verification  
- 🕵️ Fraud Detection (Deepfake, Scripted Answers)  
- 🧠 Contextual Evaluation of International Applicants  

---

## 💡 Why Prompts Matter
Prompts are the backbone of **LLM-driven evaluation systems**. They define how AI agents:

- Extract structured data from documents
- Generate semantic descriptions from video frames
- Conduct context-aware reasoning for credential equivalence
- Support explainable decision-making for human reviewers

---

## 📁 Repository Structure
```
├── admission_prompts/
│   ├── document_analysis/
│   │   ├── information_extractor_from_document_images.txt
│   │   ├── ...
│   ├── video_interview/
│   │   ├── transcription_quality.txt
│   │   ├── semantic_enrichment.txt
│   │   ├── fraud_detection.txt
│   ├── evaluation/
│   │   ├── holistic_scoring.txt
│   │   ├── follow_up_questions.txt
│   └── README.md
├── examples/
│   ├── sample_outputs/
│   ├── integration_with_pipeline.txt
└── LICENSE
```

---

## 🧾 Key Prompt Categories

### 📄 Document Analysis
- Extract applicant name, degree, institution, and graduation date
- Validate credentials using **Retrieval-Augmented Generation (RAG)** with authoritative sources (ISCED, ENIC-NARIC)

### 🎥 Video Interview
- Transcribe audio using ASR models (e.g., Whisper)
- Generate semantic descriptions of frames using Vision-Language Models (e.g., Gemini, Gemma)
- Detect inconsistencies (lip-sync, deepfake indicators)

### 🧠 Evaluation & Scoring
- Holistic scoring prompts combining text, audio, and visual cues
- Dynamic follow-up question generation for iterative interviews

---

## 🔧 Integration
These prompts are designed to work with:

- **Google Generative AI (Gemini/Gemma)** for multimodal reasoning
- **OpenAI Whisper** for speech-to-text transcription
- **RAG-based systems** for credential adjudication

---

## ▶️ Usage
Clone the repository and integrate prompts into your pipeline:

```bash
git clone https://github.com/<your-org>/fair-vid-prompts.git
cd fair-vid-prompts/admission_prompts
```

Example usage in Python:
```python
prompt = open("prompts/document_analysis/extract_credentials.txt").read()
response = llm.generate(prompt, input_image="diploma.jpg")
print(response)
```

---

## 📜 License
This repository is released under the [Creative Commons Attribution (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license.

---

## 📚 References
- [FAIR-VID: A Multimodal Pre-processing Pipeline for Applicant Video Analysis](https://doi.org/10.3390/xxxxx)
- Google Research: [Gemma 3 Developer Guide](https://blog.google/technology/developers/gemma-3/)
- UNESCO ISCED Framework: [ISCED 2011](https://uis.unesco.org/sites/default/files/documents/isced-2011-en.pdf)

