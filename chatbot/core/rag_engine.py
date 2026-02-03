import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv

try:
    from google import genai
    GEMINI_AVAILABLE = True
except Exception:
    GEMINI_AVAILABLE = False

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
KB_PATH = os.path.join(BASE_DIR, "data", "knowledge_base.txt")


class RAGEngine:
    def __init__(self):
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")
        self.documents = self._load_docs()
        self.embeddings = self.embedder.encode(self.documents)

        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))

        self.client = None
        if GEMINI_AVAILABLE and os.getenv("GEMINI_API_KEY"):
            try:
                self.client = genai.Client(
                    api_key=os.getenv("GEMINI_API_KEY")
                )
            except Exception:
                self.client = None

    def _load_docs(self):
        if not os.path.exists(KB_PATH):
            raise FileNotFoundError(f"Knowledge base not found: {KB_PATH}")

        with open(KB_PATH, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]

    def retrieve(self, query, top_k=3):
        query_vec = self.embedder.encode([query])
        _, indices = self.index.search(np.array(query_vec), top_k)
        return [self.documents[i] for i in indices[0]]

    def generate(self, query):
        retrieved_docs = self.retrieve(query, top_k=1)

        if not retrieved_docs:
            return "Sorry, I couldn’t find relevant information."

        best_answer = retrieved_docs[0]

        if not self.client:
            return best_answer

        prompt = f"""
You are a customer support assistant.
Answer the question clearly in ONE sentence using the information below.

Information:
{best_answer}

Question:
{query}
"""

        try:
            response = self.client.models.generate_content(
                model="models/gemini-1.5-pro",
                contents=prompt
            )
            return response.text
        except Exception:
            return best_answer
