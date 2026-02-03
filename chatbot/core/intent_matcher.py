import sys
from chatbot.data.intents import INTENTS
from chatbot.exception.exception import CustomerServiceException


def match_intent(user_input: str) -> dict:
    try:
        user_text = user_input.lower().strip()
        user_words = set(user_text.split())
        matched = []

        greeting_phrases = {
            "hi", "hello", "hey",
            "good morning", "good afternoon", "good evening",
            "is anyone there"
        }

        refund_phrases = {
            "money back",
            "refund not received",
            "return request",
            "cancel order",
            "cancel my order",
            "return my product",
            "i want to return my product"
        }

        shipping_phrases = {
            "shipping time",
            "delivery time",
            "shipping charges",
            "shipping cost"
        }

        hours_phrases = {
            "working hours",
            "office hours",
            "when are you open"
        }

        goodbye_phrases = {
            "bye", "goodbye",
            "see you", "see ya",
            "ok bye", "thats all"
        }

        for intent in INTENTS:
            if intent["intent"] == "greeting":
                if user_text in greeting_phrases or user_words & {"hi", "hello", "hey"}:
                    matched.append(intent)

            elif intent["intent"] == "complaint":
                if user_words & {
                    "unhappy", "frustrating", "bad",
                    "worst", "disappointed", "complaint",
                    "satisfied"
                }:
                    matched.append(intent)

            elif intent["intent"] == "refund_policy":
                if user_text in refund_phrases or user_words & {"return", "refund", "cancel"}:
                    matched.append(intent)

            elif intent["intent"] == "order_status":
                if user_words & {"order", "track", "status", "delayed", "arrive"}:
                    matched.append(intent)

            elif intent["intent"] == "shipping_info":
                if user_text in shipping_phrases or user_words & {"shipping", "delivery"}:
                    matched.append(intent)

            elif intent["intent"] == "working_hours":
                if user_text in hours_phrases or user_words & {"hours", "open", "timings"}:
                    matched.append(intent)

            elif intent["intent"] == "product_info":
                if user_words & {
                    "product", "products", "features",
                    "details", "sell",
                    "specification", "specifications"
                }:
                    matched.append(intent)

            elif intent["intent"] == "goodbye":
                if user_text in goodbye_phrases or user_words & {"bye", "goodbye"}:
                    matched.append(intent)

            elif intent["intent"] == "confirmation":
                if (
                    user_words & {"ok", "okay", "yes", "sure", "alright", "no"}
                    or (
                        "want" in user_words
                        and (
                            "dont" in user_words
                            or "not" in user_words
                            or "do not" in user_text
                        )
                    )
                    or user_text in {"not really", "sounds good"}
                ):
                    matched.append(intent)

            elif intent["intent"] == "thank_you":
                if (
                    user_words & {"thanks", "thank", "appreciate"}
                    or user_text in {"thank you", "thank you so much", "thx"}
                    or "thx" in user_text
                ):
                    matched.append(intent)

            elif intent["intent"] == "contact_support":
                if user_words & {"support", "contact", "help", "human", "agent"}:
                    matched.append(intent)

        if not matched:
            return None

        matched.sort(key=lambda x: x["priority"])
        best_intent = matched[0].copy()
        best_intent["confidence"] = 0.9 if len(matched) == 1 else 0.6

        return best_intent

    except Exception as e:
        raise CustomerServiceException(e, sys)
