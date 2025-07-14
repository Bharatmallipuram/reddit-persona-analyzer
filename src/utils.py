import re

def clean_text(text: str, max_length: int = 300) -> str:
    if not text:
        return ""
    # Remove URLs, markdown, etc.
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # markdown links
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_length] + ("..." if len(text) > max_length else "")
