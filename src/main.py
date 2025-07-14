import argparse
from urllib.parse import urlparse
from reddit_scraper import scrape_user_data
from persona_generator import generate_persona_with_ollama
import os

def extract_username_from_url(url):
    try:
        parsed_url = urlparse(url)
        parts = parsed_url.path.strip("/").split("/")
        return parts[1] if parts[0] == "user" else None
    except:
        return None

def save_persona_to_file(username, persona):
    filename = f"output/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona)
    print(f"✅ Persona saved to: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Generate a Reddit user persona from profile URL.")
    parser.add_argument("--url", required=True, help="Reddit user profile URL")

    args = parser.parse_args()
    url = args.url
    username = extract_username_from_url(url)

    if not username:
        print("❌ Invalid Reddit user URL. Use format: https://www.reddit.com/user/username/")
        return

    print(f"🔍 Scraping data for user: {username}")
    data = scrape_user_data(username)

    print(f"🤖 Generating persona using Mistral model...")
    persona = generate_persona_with_ollama(username, data["posts"], data["comments"])

    save_persona_to_file(username, persona)

if __name__ == "__main__":
    main()
