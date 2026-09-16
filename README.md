# Clinical Note Structurer

## Overview

Clinical Note Structurer is a learning-oriented project focused on the intersection of **software development, artificial intelligence, and healthcare**.

The goal is to progressively build an application capable of transforming synthetic clinical notes written in natural language into structured healthcare information.

Example:

**Input**

> Patient is 64 years old and has hypertension. The patient is currently taking Ramipril.

**Structured output**

```text
Age: 64
Condition: Hypertension
Medication: Ramipril
```

The project is developed incrementally, starting from core Python concepts and gradually introducing structured data, APIs, AI integration, user interface development, and healthcare interoperability standards.

This project uses only synthetic or appropriate public data. No real patient information is used.

---

## Learning Objectives

The primary objective of this project is to develop practical skills that complement a theoretical Computer Science background, with particular attention to AI applications in healthcare.

### Software Development

* Apply Python to a complete project
* Work with data structures and functions
* Read and write JSON data
* Use external Python libraries
* Develop debugging and error-handling skills
* Organize a small software project

### Artificial Intelligence

* Understand how existing AI models can be integrated into applications
* Interact with Large Language Models through APIs
* Design prompts for structured information extraction
* Work with structured model outputs
* Explore the limitations and reliability of AI-generated information

### Healthcare Technology

* Understand the basics of structured healthcare data
* Explore healthcare interoperability
* Gain an introduction to FHIR
* Examine potential applications of AI within healthcare workflows
* Consider privacy, reliability, and responsible AI principles in healthcare

### Development Tools

* Visual Studio Code
* Git and GitHub
* Python virtual environments
* Python package management
* REST APIs
* JSON
* Streamlit

---
## Setup

### 1. Clone the Repository

Clone the repository and move into the project directory.

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

The `.venv` directory contains the local Python environment and installed dependencies. It is excluded from version control and should not be committed to GitHub.

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

The project currently uses:

- `google-genai` to interact with the Gemini API.
- `python-dotenv` to load environment variables from a local `.env` file.

### 4. Configure the Gemini API Key

Create a `.env` file in the root directory of the project:

```text
GEMINI_API_KEY=your_api_key_here
```

The API key is loaded at runtime and is never stored directly in the Python source code.

The `.env` file contains sensitive credentials and is excluded from version control through `.gitignore`.

**Never commit API keys or other secrets to the repository.**

### 5. Local Files Excluded from Git

The following files and directories are intentionally excluded from version control:

```text
.env
.venv/
__pycache__/
```

- `.env` stores local environment variables and secrets.
- `.venv/` contains the local Python virtual environment and installed packages.
- `__pycache__/` contains automatically generated Python bytecode.

---

## Project Roadmap

### Phase 1 — Python Foundations

Build the core application logic while strengthening practical Python skills.

### Phase 2 — Structured Data

Represent clinical information using Python data structures and JSON.

### Phase 3 — AI Integration

Integrate an existing Large Language Model through an API to extract structured information from synthetic clinical notes.

### Phase 4 — Application Interface

Develop a simple user interface that allows users to submit a clinical note and visualize the structured output.

### Phase 5 — Healthcare Interoperability

Explore FHIR concepts and investigate how extracted information can be represented using standardized healthcare data structures.

---

## Project Purpose

This project serves both as a technical learning exercise and as an exploration of career paths at the intersection of **Computer Science, Artificial Intelligence, and Healthcare**.

The focus is not on training machine learning models from scratch, but on understanding how existing AI technologies can be integrated, evaluated, and applied to real-world healthcare problems.
