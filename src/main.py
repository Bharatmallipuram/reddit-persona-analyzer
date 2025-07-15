# Modules
import os
import argparse
from reddit_scraper import scrape_user_data
from persona_generator import generate_persona_with_ollama
from logger import setup_logger
from rich.console import Console

logger = setup_logger()
console = Console()

def save_output(username, content):
    os.makedirs("output", exist_ok=True)   # Creates the output folder if it doesnt exist.
    filename = f"output/{username}_persona.txt"
    with open(filename, "w", encoding="utf-8") as f:   # ensures the content is read exactly without loosing and of special characters or symbols.
        f.write(content)
    logger.info(f" Persona saved to: {filename}")
    console.print(f"[bold green] Persona saved to:[/bold green] [white]{filename}[/white]")

def main():
    logger.info(" Persona Generator started.")
    logger.info(" Starting persona generation")
    logger.debug(" This debug message will show only if DEBUG level is enabled")

    parser = argparse.ArgumentParser(description="Generate Reddit User Persona using Ollama")
    parser.add_argument("--username", required=True, help="Reddit username (without /user/)")
    parser.add_argument("--model", default="tinyllama", help="Ollama model name to use")
    args = parser.parse_args()

    username = args.username
    model = args.model

    logger.info(f" Starting user persona generation for '{username}' using model: {model}")
    console.print(f"[bold cyan] Scraping data for user:[/bold cyan] {username}")

    try:
        data = scrape_user_data(username)
    except Exception as e:
        logger.error(f" Error scraping Reddit user '{username}': {e}")
        console.print(f"[bold red] Error scraping user data:[/bold red] {e}")
        return

    try:
        persona = generate_persona_with_ollama(username, data["posts"], data["comments"], model=model)
        save_output(username, persona)
    except Exception as e:
        logger.error(f" Error generating persona: {e}")
        console.print(f"[bold red] Error generating persona:[/bold red] {e}")

    console.print("[bold magenta] Persona generation complete! Check the output folder.[/bold magenta]")

if __name__ == "__main__":
    main()
