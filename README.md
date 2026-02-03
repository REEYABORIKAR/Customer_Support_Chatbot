Customer Support Chatbot 🤖
A hybrid customer support chatbot built with FastAPI. This bot combines rule-based intent recognition with a Retrieval-Augmented Generation (RAG) engine powered by FAISS and Gemini AI to provide accurate and natural responses to customer inquiries.

🚀 Features
Hybrid Intent Recognition: Uses a rule-based system for common tasks (greetings, order tracking) and a RAG engine for complex queries.

RAG Engine (Retrieval-Augmented Generation): Leverages FAISS for vector search and Sentence Transformers to retrieve relevant information from a local knowledge base.

Gemini AI Integration: Generates human-like, single-sentence responses using Google's Gemini 1.5 Pro model when an API key is provided.

Order Tracking Simulation: Implements multi-turn logic to request and validate order IDs (5–20 alphanumeric characters).

Advanced Text Preprocessing: Normalizes text, removes special characters, and utilizes pyspellchecker alongside custom corrections for common typos.

Web-Based Interface: Real-time interaction via a clean UI built with HTML/CSS and JavaScript.

Robust Error Handling: Features custom exception management and session-based logging for debugging.

🛠️ Tech Stack
Backend: FastAPI

AI/ML: Google GenAI (Gemini 1.5 Pro), FAISS, Sentence-Transformers

Templating: Jinja2

Spelling Correction: pyspellchecker

Frontend: HTML5, CSS3, JavaScript

📋 Prerequisites
Python 3.8+

pip (Python package manager)

(Optional) Gemini API Key for advanced responses

⚙️ Installation & Setup
Clone the repository:

Bash
git clone https://github.com/REEYABORIKAR/Customer_Support_Chatbot.git
cd Customer_Support_Chatbot
Create a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

Bash
pip install -r requirements.txt
Configure Environment Variables: Create a .env file in the root directory and add your API key to enable Gemini AI:

Plaintext
GEMINI_API_KEY=your_gemini_api_key_here
Run the application:

Bash
uvicorn app:app --reload
Access the Chatbot: Navigate to http://127.0.0.1:8000 in your browser.

💬 Supported Scenarios
Greetings: Hello, Hi, Hey.

Order Status: Tracking and checking delivery (requires valid ID).

Refunds: Information on policies and processing times.

Shipping: Delivery charges and estimated timelines.

Complaints: Handling customer feedback and frustrations.

General Inquiry: Working hours (Mon–Fri, 9 AM – 6 PM), product info, and support contact.

📁 Project Structure
Plaintext
├── app.py                # FastAPI application entry point
├── chatbot/
│   ├── core/             
│   │   ├── chatbot_engine.py # Main logic coordinator
│   │   ├── intent_matcher.py # Rule-based keyword matching
│   │   └── rag_engine.py     # FAISS retrieval and Gemini generation
│   ├── config/           # App settings and constants
│   ├── data/             
│   │   ├── intents.py        # Predefined intent patterns
│   │   └── knowledge_base.txt # RAG source documents
│   ├── exception/        # Custom error handling
│   ├── logging/          # Logging configuration
│   └── utils/            # Text cleaning and validation
├── static/               # Frontend assets (CSS/JS)
├── templates/            # HTML templates
├── .env                  # API keys (not included in repo)
└── requirements.txt      # Project dependencies