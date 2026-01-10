# 🧠 GenAI Agent for Universal Data Quality Scoring

## 💬 With Conversational Chatbot for Speaking with Data (Payments Domain)

Payment organizations process massive volumes of transaction and operational data every day. However, there is **no universal, objective, and explainable way** to evaluate data quality across standard dimensions such as completeness, accuracy, consistency, timeliness, uniqueness, validity, and integrity.

Additionally, **non-technical users cannot interact with data directly**. They depend on engineers to answer basic questions like:

* “Is this dataset reliable?”
* “Why is this report failing?”
* “Which fields are risky for compliance?”

---

## 🎯 Objective

To build a **GenAI-powered Data Quality Agent with an Interactive Chatbot** that allows users to:

* Upload **any dataset securely**
* Automatically compute **dimension-wise Data Quality Scores**
* Generate a **composite Data Quality Score (DQS)**
* **Chat with the data in natural language**
* Receive **plain-English explanations and recommendations**
* Ensure **privacy, governance, and compliance**

---

## 💡 Solution Overview

This project delivers a **Conversational Data Quality Intelligence Platform**.

### 🔑 Core Innovation

> A **chatbot that understands data quality metrics and metadata**, allowing users to *talk to their dataset* instead of reading complex reports.

Think of it as:

* 🗣️ **ChatGPT for Data Quality**
* 📊 **Credit Score + Doctor + Assistant for Data**
* 🏦 **Trust layer for payments data**

---

## 💬 Conversational Chatbot (Main Feature)

### 🧠 What the Chatbot Can Do

The chatbot is powered by **GenAI + RAG (Retrieval-Augmented Generation)** and can answer questions such as:

* “What is the overall quality of this dataset?”
* “Why is the completeness score low?”
* “Which columns are causing consistency issues?”
* “Is this dataset safe for regulatory reporting?”
* “What should I fix first to improve the score?”
* “Explain the risks in simple terms.”

### 🗣️ Example Chat Interaction

**User:**

> Why is the data quality score only 62?

**Chatbot:**

> The score is low mainly due to missing values in KYC address fields and duplicate transaction IDs. This can impact compliance checks and settlement accuracy. Improving these two areas could increase the score by approximately 18 points.

---

## 🧩 Key Capabilities

### ✔ Secure Dataset Ingestion

* CSV / Excel / JSON supported
* No raw data storage
* Metadata-only processing

### ✔ Automatic Dimension Identification

The system dynamically identifies which data quality dimensions apply based on dataset structure and context.

### ✔ Data Quality Scoring Engine

Scores computed for:

* Completeness
* Accuracy
* Consistency
* Timeliness
* Uniqueness
* Validity
* Integrity

### ✔ Composite Data Quality Score (DQS)

* Unified score from **0–100**
* Represents overall dataset trustworthiness

### ✔ GenAI Chatbot for Data Interaction

* Natural language Q&A
* Business-friendly explanations
* Context-aware insights (payments domain)
* No SQL or technical knowledge required

### ✔ Actionable Recommendations

* Prioritized fixes
* Step-by-step guidance
* Regulatory and business impact awareness

---

## 🧠 Data Quality Dimensions Explained

| Dimension        | Meaning                            |
| ---------------- | ---------------------------------- |
| **Completeness** | Missing or null values             |
| **Accuracy**     | Correctness of data                |
| **Consistency**  | Conflicting values across columns  |
| **Timeliness**   | Data freshness                     |
| **Uniqueness**   | Duplicate records                  |
| **Validity**     | Rule and format compliance         |
| **Integrity**    | Relationship and dependency checks |

---

## 🏗️ High-Level Architecture

**System Flow:**

1. Secure Data Upload
2. Metadata Extraction
3. Rule-Based & Statistical Profiling
4. Dimension-Level Scoring
5. Composite DQS Calculation
6. Metadata Indexing (Vector Store)
7. GenAI Chatbot (RAG-based Reasoning)
8. Interactive Dashboard & Chat Interface

---

## 🤖 Role of Generative AI

GenAI is used to:

* Interpret data quality metrics
* Answer user questions conversationally
* Convert technical issues into business language
* Provide compliance-aware explanations
* Recommend improvements interactively

Example:

> “Low integrity between transaction and settlement tables may lead to reconciliation failures and audit risks.”

---

## 🔐 Privacy, Security & Governance

Designed specifically for the **payments domain**:

* ❌ No transaction data persisted
* ✅ Metadata-only analysis
* ✅ Sensitive fields masked or hashed
* ✅ Chatbot operates on scores & metadata only
* ✅ Audit-friendly outputs

Aligned with:

* PCI-DSS principles
* GDPR privacy guidelines

---

## 🧑‍💻 Tech Stack

### Backend & Processing

* Python
* Pandas
* NumPy

### GenAI & Chatbot
* LLaMA (Meta AI)
* Hugging Face Transformers
* RAG (Retrieval-Augmented Generation)
* Vector embeddings (FAISS)

### Data Quality Logic

* Rule-based validation
* Statistical profiling

### UI & Interaction

* Streamlit
* Integrated Chat Interface
* Plotly dashboards

### Deployment

* Google Colab / Local execution
* GitHub-hosted repository

---
### 4️⃣ Use the Chatbot

* Upload a dataset
* Ask questions in natural language
* Explore scores, insights, and fixes interactively

---

## 📊 Outputs Provided

* Overall Data Quality Score (DQS)
* Dimension-wise score breakdown
* Interactive visual dashboards
* Conversational chatbot responses
* Actionable improvement recommendations

---

## 🏦 Why This Is Valuable for Payments & Visa

* Makes data quality **transparent and measurable**
* Enables **non-technical stakeholders** to interact with data
* Reduces dependency on manual investigations
* Improves regulatory confidence
* Scales across datasets, teams, and regions

This solution can evolve into a **platform-level data trust service**.

---

## 🔮 Future Enhancements

* Real-time streaming data chatbot
* Autonomous agent-based remediation
* Industry-wide DQS benchmarking
* API-first integration
* Multi-language chatbot support

---

## 🏁 Conclusion

> **“Data is only valuable when it is trusted.”**

By combining **data quality scoring with a conversational GenAI chatbot**, this project transforms complex datasets into **trusted, explainable, and interactive intelligence** for the payments ecosystem.

---

## 📜 License

Developed for educational and hackathon purposes under Shaastra 2026 guidelines.