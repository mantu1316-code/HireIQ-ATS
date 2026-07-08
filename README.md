# ⚡ HireIQ — AI Resume Screening Intelligence Engine

[![Inference Engine](https://img.shields.io/badge/Inference%20Engine-Llama%203.1-blueviolet)](https://groq.com/)
[![API Acceleration](https://img.shields.io/badge/API-Groq%20Cloud-orange)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)

An enterprise-grade, high-intelligence Applicant Tracking System (ATS) optimization portal. HireIQ normalizes raw, multi-format digital resumes (PDF, DOCX, TXT) using structural NLP tokenization, builds capability vectors, and dispatches them across rapid inference pathways to map candidate alignment metrics against any complex target Job Description.

🔗 **Active Production Remote API Endpoint:** `https://hireiq-ats.onrender.com/screen`

---

## 🚀 Architectural Blueprint & Processing Pipeline

HireIQ leverages a deterministic execution strategy broken down into four distinct micro-frontend layers:

1. **Extraction Sandbox:** Synchronous document ingestion utilizing `pdf.js` and binary buffer text parsing (`mammoth.browser`) directly on client-side vectors before streaming payloads.
2. **NLP Normalization Matrix:** Raw structural extraction that handles irregular data layouts, sanitizes text strings, and creates normalized token matrices.
3. **Inference Context Router:** Dispatches parallel multi-candidate payloads to an accelerated cloud compiler powered by **Groq Cloud API** running ultra-fast **Llama 3.1 models**.
4. **Weighted Scoring Matrix:** Generates deterministic analytical output metrics scored out of 100 based on core technical stack alignment, relative structural experience depth, and contextual seniority flags.

---

## 📊 Evaluation Vector Breakdown

The analytical system categorizes candidates across multi-dimensional criteria displayed on a responsive cross-platform dashboard interface:

| Matrix Criterion | Technical Sub-System Scope | UI Element / Representation |
| :--- | :--- | :--- |
| **Similarity Score** | Global context semantic match threshold. | Color-coded dynamic filling progress bars. |
| **Stack Alignment** | Hard keywords, skill-dense vectors, and runtime stack validation. | Automated `Shortlisted` / `Under Review` validation chips. |
| **Experience Profile** | Scale-based temporal tracking computed against targeted role parameters. | Modular metrics card block. |
| **Core Evaluation Summary** | LLM-generated contextual explanation of structural fit/gap mapping. | Left-bordered clean typographical summary block. |

---

## 🛠️ Local Environment Bootstrapping & Setup

Follow these system setup protocols to run the frontend tracking server inside an isolated local runtime context:

### 1. Repository Synchronization
Clone the tracking code structure from the primary remote branch:
```bash
git clone [https://github.com/mantu1316-code/HireIQ-ATS.git](https://github.com/mantu1316-code/HireIQ-ATS.git)
cd HireIQ-ATS
