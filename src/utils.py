import re

def clean_text(text: str, max_length: int = 300) -> str:
    """
    Clean and truncate Reddit text:
    - Removes URLs, markdown, and extra whitespace.
    - Truncates to max_length characters.
    """
    if not text:
        return ""
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"\[.*?\]\(.*?\)", "", text)  # Remove markdown links
    text = re.sub(r"\s+", " ", text).strip()
    return text[:max_length] + ("..." if len(text) > max_length else "")

def format_for_citation(item: dict, index: int, item_type: str = "Post") -> str:
    """
    Format a clean citation line with subreddit and permalink.
    """
    subreddit = item.get("subreddit", "unknown")
    permalink = item.get("permalink", "")
    url = f"https://reddit.com{permalink}" if permalink else "N/A"
    return f"↳ Source: {item_type} {index + 1} – r/{subreddit} ({url})"
