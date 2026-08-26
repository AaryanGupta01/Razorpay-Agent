# 📊 RAG Document Analyzer & Assistant

A responsive, full-page AI Assistant built using **Flowise**, **Pinecone Vector Database**, and **Flask**. This tool allows users to dynamically upload documents (PDFs, TXT, DOCX, CSV) directly through a web interface, vectors them using **Google Gemini Embeddings**, and provides real-time intelligent analysis and summarization using **Mistral AI** via a custom-designed Conversational RAG pipeline.

🔗 **Live Demo:** [rag-document-analyzer-4ox8.onrender.com](https://rag-document-analyzer-4ox8.onrender.com/)

---

## 🚀 Key Features

* **Dynamic Frontend Document Uploads:** Enabled a seamless file attachment mechanism directly within the chat window to parse user-provided files on the fly.
* **Vectorized Document Storage:** Replaced volatile in-memory stores with **Pinecone Vector Database** using **768-dimension Cosine similarity metrics** matching `gemini-embedding-001`.
* **Persistent User Sessions:** Automated workspace isolation by mapping dynamic frontend metadata uploads to specific conversational session IDs via a `ConversationalRetrievalQAChain`.
* **Toggleable Dark / Light Mode Switch:** Implemented a state-management controller that destroys and remounts the hidden Shadow DOM components of the chatbot to completely change look-and-feel smoothly mid-conversation.
* **Production Guardrails:** Configured fully decoupled client/server variable structures to isolate critical Chatflow endpoints safely away from public exposure.

---

## 🛠️ Tech Stack

* **Frontend UI:** Vanilla HTML5, Advanced CSS3 Transitions, JavaScript (ES6+ Module Imports)
* **Backend Interface:** Python, Flask, Gunicorn (WSGI Production Server)
* **Orchestration & RAG Canvas:** Flowise AI
* **Vector DB:** Pinecone (Serverless)
* **Models Utilized:** * *Embeddings:* Google Gemini (`gemini-embedding-001`)
    * *LLM:* Mistral AI (`mistral-tiny`)

---

## 📁 Repository Structure

├── app.py                 # Core Flask backend application & configurations route
├── templates/
│   └── index.html         # Full-page frontend interface & custom UI toggle handler
├── requirements.txt       # Production dependencies for web server deployment
├── .gitignore             # Strict staging blocks to avoid private tracking leaks
└── README.md              # Project roadmap & structural documentation

1. Clone the Workspace
Bash

git clone [https://github.com/your-username/rag-document-analyzer.git](https://github.com/your-username/rag-document-analyzer.git)
cd rag-document-analyzer

2. Set Up Your Python Environment
Bash

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt

3. Launch the App Locally
Bash

flask run

Your local server will boot at http://127.0.0.1:5000/.
