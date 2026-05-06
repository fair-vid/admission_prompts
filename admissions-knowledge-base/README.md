# Admissions Knowledge Base

This repository contains a structured knowledge base for transparent, auditable, and reproducible AI-assisted international admissions workflows.

The repository stores machine-readable knowledge artifacts used by admissions agents, document-understanding pipelines, grading interpretation modules, and process-level decision-support systems. Its purpose is to make admissions knowledge explicit, version-controlled, inspectable, and reusable across notebook-based prototypes and production digital-twin deployments.

## Purpose

International admissions require interpretation of heterogeneous educational documents from many countries, including secondary-school certificates, state examination results, grading scales, transcripts, and country-specific admission requirements. In AI-assisted admissions systems, this contextual knowledge must be available in a transparent and auditable form.

This repository provides a central place for such knowledge.

The knowledge base supports:

- interpretation of international secondary-school qualifications;
- recognition of required documents after high school;
- description of national grading systems and passing thresholds;
- mapping between local grading schemes and normalized scales;
- prompt templates for document-understanding and reasoning agents;
- JSON schemas for structured outputs;
- validation examples and test cases;
- transparent review of assumptions used by AI agents.

The repository is designed for use in transparent admissions architectures where AI agents do not make hidden end-to-end decisions, but instead transform documents, transcripts, video signals, and structured application data into explicit, auditable evidence variables. This follows the digital-twin and transparency-by-design approach described in the accompanying research framework, where notebook-based agents expose intermediate artifacts, prompts, and decision logic for inspection. [1](https://vgtuitsc-my.sharepoint.com/personal/algirdas_laukaitis_vilniustech_lt/Documents/%E2%80%9EMicrosoft%20Copilot%E2%80%9C%20pokalbi%C5%B3%20failai/PeerJ_submission_fv.pdf)

## Context

This knowledge base is part of a broader transparent admissions framework based on:

- modular AI agents;
- notebook-based reproducibility;
- local or institutionally controlled execution;
- process-mined digital twins of real admissions workflows;
- transparent prompts and intermediate artifacts;
- interpretable downstream decision models such as decision trees.

The framework is motivated by the need to avoid opaque cloud-only decision systems in high-stakes admissions. In the associated paper, admissions workflows are treated as process-centric digital twins where visual document understanding, video interview analysis, and structured application data are processed by separate agents and then integrated into auditable state-transition models. [1](https://vgtuitsc-my.sharepoint.com/personal/algirdas_laukaitis_vilniustech_lt/Documents/%E2%80%9EMicrosoft%20Copilot%E2%80%9C%20pokalbi%C5%B3%20failai/PeerJ_submission_fv.pdf)

A key idea is that AI agents require contextual knowledge to interpret educational credentials correctly. For example, a document-understanding agent must not only read OCR text from a diploma, but also understand what type of qualification it is, which country issued it, what grading scale applies, and whether final school examinations or university entrance examinations are normally required. [1](https://vgtuitsc-my.sharepoint.com/personal/algirdas_laukaitis_vilniustech_lt/Documents/%E2%80%9EMicrosoft%20Copilot%E2%80%9C%20pokalbi%C5%B3%20failai/PeerJ_submission_fv.pdf)

## What This Repository Stores

This repository may contain several types of knowledge-base files.

### 1. Country-level admissions requirements

Files describing national or education-system-specific requirements after high school, for example:

- name of the secondary qualification;
- required documents;
- final examination or centralized examination requirements;
- language and translation requirements;
- admission-relevant notes;
- special cases and institution-specific conditions.

Example file type:

```text
kb/countries/international_bachelor_requirements.json
