import re
import sys
from spellchecker import SpellChecker
from chatbot.exception.exception import CustomerServiceException
from chatbot.logging.logger import logging

spell = SpellChecker()

# Custom typo corrections (domain-specific)
CUSTOM_CORRECTIONS = {
    "bas": "bad",
    "servic": "service",
    "retrun": "return",
    "thnks": "thanks",
    "wher": "where",
    "shippng": "shipping",
    "delivry": "delivery",
    "frustratd": "frustrated"
}


def clean_text(text: str) -> str:
    """
    Normalize, clean, and correct spelling in user input
    """
    try:
        text = text.lower()
        text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

        corrected_words = []
        for word in text.split():
            if word in CUSTOM_CORRECTIONS:
                corrected_words.append(CUSTOM_CORRECTIONS[word])
            else:
                corrected_words.append(spell.correction(word) or word)

        cleaned_text = " ".join(corrected_words).strip()
        logging.info(f"Cleaned input: {cleaned_text}")
        return cleaned_text

    except Exception as e:
        raise CustomerServiceException(e, sys)


def validate_input(text: str):
    """
    Validate user input before processing

    Returns:
        (bool, str | None)
        False, "empty"    -> empty input
        False, "too_long" -> input too long
        True, None        -> valid input
    """
    try:
        if not text or len(text.strip()) == 0:
            return False, "empty"

        if len(text) > 300:
            return False, "too_long"

        return True, None

    except Exception as e:
        raise CustomerServiceException(e, sys)
