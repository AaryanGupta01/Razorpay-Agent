# 🚀 Razorpay Agentic Commerce Pipeline

[![Live Demo](https://img.shields.io/badge/Live_Demo-Available-00E676?style=for-the-badge)](https://razorpay-agent-5h5z.onrender.com/)
[![Tech Stack](https://img.shields.io/badge/Python-Flask-3366FF?style=for-the-badge&logo=python&logoColor=white)]()
[![Tech Stack](https://img.shields.io/badge/Flowise-LLM_Orchestration-8B5CF6?style=for-the-badge)]()

**Live Application:** [https://razorpay-agent-5h5z.onrender.com/](https://razorpay-agent-5h5z.onrender.com/)

## 📌 Overview
This project is a full-stack, voice-activated AI financial support engineer designed to solve two critical pain points for Tier-2 and Tier-3 merchants in India: tracking failed payments and decoding complex financial documents (like MDR tax invoices and Settlement reports) despite language barriers.

Instead of a simple chatbot, this system implements **Agentic Routing**. The AI autonomously decides whether to execute a live API action or query a vector database based on the user's intent.

## ✨ Key Features
*   **🎙️ Multilingual Voice Interface:** Captures audio directly from the browser and transcribes regional Indian languages (Hindi, Marathi, Tamil, etc.) to text using the **Sarvam AI (saaras:v3)** API.
*   **⚙️ Autonomous Tool Calling:** If a user asks about a failed payment (e.g., *"9876543210 ka payment kyu fail hua?"*), the agent securely hits the Flask backend to query the live **Razorpay API**, diagnoses the exact error, and generates a payment recovery link.
*   **📄 Document Intelligence (RAG):** Merchants can upload dense English PDFs (Tax Invoices, Settlement ledgers). The agent searches the embedded vector database and explains specific line items conversationally in the user's native language.
*   **💻 Glassmorphic FinTech UI:** A custom, fully responsive frontend tailored to Razorpay's design system (Deep Navy, True Blue, and Success Green) with dynamic typewriter animations and custom injected CSS for the Flowise widget.

## 🏗️ System Architecture
1.  **Frontend:** Custom HTML/JS interface with a dedicated microphone component that securely accesses the user's local audio stream.
2.  **Transcription Layer:** Audio chunks are sent to a Flask endpoint (`/v1/audio/transcriptions`), mapped to the Sarvam AI API for highly accurate regional speech-to-text.
3.  **Agentic Router (Flowise):** The transcribed text is passed to a Flowise LLM Agent which acts as the brain.
    *   *Path A (Action):* Routes to the Custom Tool hitting the Flask `/api/diagnose_and_recover` endpoint.
    *   *Path B (Knowledge):* Routes to the Vector Store (In-Memory/Pinecone) containing document embeddings.
4.  **Backend:** Python/Flask server deployed on Render, managing API integrations and serving the UI.

## 🛠️ Tech Stack
*   **Backend:** Python, Flask, Razorpay Python SDK
*   **AI/LLM:** Flowise (LangChain), Sarvam AI (Speech-to-Text), OpenAI (Embeddings/LLM)
*   **Frontend:** HTML5, CSS3, Vanilla JavaScript, Flowise Embed API
*   **Deployment:** Render (Cloud Hosting)

## 🚀 Local Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt

RAZORPAY_KEY_ID=your_test_key_id
RAZORPAY_KEY_SECRET=your_test_key_secret
SARVAM_API_KEY=your_sarvam_key

flask run
```
## 💡 Usage Example

Scenario 1: Live API Recovery

Action: Click the mic and dictate: "Check the payment status for 9876543210"

Result: The agent fetches the live Razorpay diagnostic, explains the failure reason (e.g., CVV mismatch), and provides a recovery payment link.

Scenario 2: Multilingual Document Q&A

Action: Upload an English "MDR & Tax Invoice" PDF.
Action: Click the mic and dictate in Hindi: "Mera is mahine ka platform fee kitna laga hai?"

Result: The agent retrieves the specific chunk from the vector database and replies accurately in Hindi.

Designed & Developed by Aaryan Gupta
