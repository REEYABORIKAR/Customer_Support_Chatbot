import random
import sys

from chatbot.utils.text_utils import clean_text, validate_input
from chatbot.core.intent_matcher import match_intent
from chatbot.config.setting import FALLBACK_MESSAGE, EXIT_KEYWORDS
from chatbot.exception.exception import CustomerServiceException


def is_valid_order_id(order_id: str) -> bool:
    return order_id.isalnum() and 5 <= len(order_id) <= 20


class ChatbotEngine:

    def __init__(self):
        self.awaiting_order_id = False

    def process_message(self, message: str) -> str:
        try:
            valid, reason = validate_input(message)

            if not valid:
                if reason == "empty":
                    return "Please enter a message so I can help you."
                if reason == "too_long":
                    return "Your message is too long. Please keep it under 300 characters."

            cleaned_message = clean_text(message)

            if cleaned_message == "":
                return "Please use words or numbers so I can understand you."

            if cleaned_message in EXIT_KEYWORDS:
                return "exit"

            if self.awaiting_order_id:
                if cleaned_message.isalnum() and is_valid_order_id(cleaned_message):
                    self.awaiting_order_id = False
                    return (
                        f"Thanks! I’ve received your order ID {cleaned_message}. "
                        "Our team is checking the status."
                    )
                else:
                    return "Please provide a valid order ID (numbers or letters)."

            intent = match_intent(cleaned_message)

            if intent is None:
                return random.choice(FALLBACK_MESSAGE)

            if intent["intent"] == "order_status":
                self.awaiting_order_id = True

            return random.choice(intent["responses"])

        except Exception as e:
            raise CustomerServiceException(e, sys)
