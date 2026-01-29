import sys
from chatbot.data.intents import INTENTS
from chatbot.exception.exception import CustomerServiceException


def match_intent(user_input: str) -> dict:
    try:
        user_words = set(user_input.split())
        matched = []

        for intent in INTENTS:

            # ---------- GREETING ----------
            if intent["intent"] == "greeting":
                if user_words & {"hi", "hello", "hey"} and len(user_words) <= 3:
                    matched.append(intent)

            # ---------- COMPLAINT / NEGATIVE FEEDBACK ----------
            elif intent["intent"] == "complaint":
                if user_words & {
                    "unhappy", "frustrating", "bad",
                    "worst", "disappointed", "complaint"
                }:
                    matched.append(intent)

            # ---------- REFUND / RETURN ----------
            elif intent["intent"] == "refund_policy":
                if user_words & {"return", "refund", "cancel"}:
                    matched.append(intent)

            # ---------- ORDER STATUS ----------
            elif intent["intent"] == "order_status":
                if user_words & {
                    "order", "track", "status",
                    "delayed", "arrive"
                }:
                    matched.append(intent)

            # ---------- SHIPPING INFO ----------
            elif intent["intent"] == "shipping_info":
                if user_words & {"shipping", "delivery"}:
                    matched.append(intent)

            # ---------- WORKING HOURS ----------
            elif intent["intent"] == "working_hours":
                if user_words & {"hours", "open", "timings"}:
                    matched.append(intent)

            # ---------- PRODUCT INFO ----------
            elif intent["intent"] == "product_info":
                if user_words & {
                    "product", "products", "features",
                    "details", "sell", "specification"
                }:
                    matched.append(intent)

            # ---------- CONFIRMATION / ACK ----------
            elif intent["intent"] == "confirmation":
                if user_words & {
                    "ok", "okay", "yes", "sure",
                    "alright", "no"
                }:
                    matched.append(intent)

            # ---------- THANK YOU ----------
            elif intent["intent"] == "thank_you":
                if user_words & {
                    "thanks", "thank", "appreciate", "thx"
                }:
                    matched.append(intent)

            # ---------- CONTACT SUPPORT ----------
            elif intent["intent"] == "contact_support":
                if user_words & {
                    "support", "contact", "help",
                    "human", "agent"
                }:
                    matched.append(intent)

            # ---------- GOODBYE ----------
            elif intent["intent"] == "goodbye":
                if user_words & {"bye", "goodbye", "see", "exit"}:
                    matched.append(intent)

        if not matched:
            return None

        # Priority-based resolution (lower number = higher priority)
        matched.sort(key=lambda x: x["priority"])
        return matched[0]

    except Exception as e:
        raise CustomerServiceException(e, sys)
