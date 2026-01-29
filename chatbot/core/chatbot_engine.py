import random
from chatbot.utils.text_utils import clean_text, validate_input
from chatbot.core.intent_matcher import match_intent
from chatbot.config.setting import FALLBACK_MESSAGE, EXIT_KEYWORDS


def is_valid_order_id(order_id: str) -> bool:
    return order_id.isalnum() and 5 <= len(order_id) <= 20


class ChatbotEngine:

    def __init__(self):
        self.awaiting_order_id = False

    def process_message(self, message: str) -> str:
        valid, reason = validate_input(message)

        if not valid:
            if reason == "empty":
                return "Please enter a message so I can help you."
            if reason == "too_long":
                return "Your message is too long. Please keep it under 300 characters."

        cleaned = clean_text(message)

        if cleaned == "":
            return "Please use words or numbers so I can understand you."

        if cleaned in EXIT_KEYWORDS:
            return "exit"

        if self.awaiting_order_id:
            if is_valid_order_id(cleaned):
                self.awaiting_order_id = False
                return f"Thanks! I’ve received your order ID {cleaned}. Our team is checking the status."
            else:
                return "That doesn’t look like a valid order ID."

        intent = match_intent(cleaned)

        if intent is None:
            return random.choice(FALLBACK_MESSAGE)

        if intent["intent"] == "order_status":
            self.awaiting_order_id = True

        return random.choice(intent["responses"])
