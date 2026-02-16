import re


def clean_text(text):
    # Keep line breaks first
    text = text.replace("\r", "\n")

    # Remove weird unicode
    text = re.sub(r"[^\x00-\x7F]+", " ", text)

    # Fix multiple spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()
