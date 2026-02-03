import random
import sys

from chatbot.utils.text_utils import clean_text, validate_input
from chatbot.core.intent_matcher import match_intent
from chatbot.config.setting import EXIT_KEYWORDS
from chatbot.exception.exception import CustomerServiceException
from chatbot.core.rag_engine import RAGEngine


def is_valid_order_id(order_id: str) -> bool:
    return order_id.isalnum() and 5 <= len(order_id) <= 20


def needs_explanation(text: str) -> bool:
    keywords = {
        "why",
        "explain",
        "how",
        "what happens",
        "reason",
        "process",
        "timeline"
    }
    return any(k in text for k in keywords)


class ChatbotEngine:

    def __init__(self):
        self.awaiting_order_id = False
        self.rag = RAGEngine()

    def process_message(self, message: str) -> str:
        try:
            valid, _ = validate_input(message)
            if not valid:
                return "Please enter a valid message."

            cleaned_message = clean_text(message)

            if cleaned_message in EXIT_KEYWORDS:
                return "exit"

            if self.awaiting_order_id:
                if is_valid_order_id(cleaned_message):
                    self.awaiting_order_id = False
                    return f"Thanks! Order ID {cleaned_message} received."
                return "Please provide a valid order ID."

            if "refund" in cleaned_message:
                return self.rag.generate(cleaned_message)

            intent = match_intent(cleaned_message)

            if needs_explanation(cleaned_message):
                return self.rag.generate(cleaned_message)

            if intent and intent.get("confidence", 1.0) >= 0.8:
                if intent["intent"] == "order_status":
                    self.awaiting_order_id = True
                return random.choice(intent["responses"])

            return self.rag.generate(cleaned_message)

        except Exception as e:
            raise CustomerServiceException(e, sys)
