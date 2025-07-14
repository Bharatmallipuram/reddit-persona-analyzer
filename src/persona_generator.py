from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import ollama
from utils import clean_text

console = Console()

def generate_prompt(username, posts, comments):
    combined_text = ""

    for i, post in enumerate(posts[:3]):
        text = clean_text(post['selftext'], max_length=300)
        combined_text += (
            f"\n[Post {i+1} - r/{post['subreddit']}]\n"
            f"Title: {post['title']}\n{text}\n"
        )

    for i, comment in enumerate(comments[:2]):
        text = clean_text(comment['body'], max_length=300)
        combined_text += (
            f"\n[Comment {i+1} - r/{comment['subreddit']}]\n{text}\n"
        )

    prompt = f"""
You are an expert language model tasked with analyzing Reddit activity to build psychological user personas.

Your goal is to infer a detailed yet concise **user profile** for the Redditor: **{username}**

From the content provided below, extract:

1. 🧠 **Interests**  
2. 💬 **Writing Style** (e.g., formal, casual, sarcastic)  
3. 🤔 **Personality Traits** (e.g., curious, introverted, opinionated)  
4. 🌍 **Stated Opinions or Beliefs** (e.g., social, political, moral views)  
5. 👤 **Demographic Clues** (only if clearly implied, e.g., student, parent, country)  

Each insight must be followed by a **citation** to the post/comment number and subreddit.  
Use this format:

↳ Source: Post 2 (r/science), Comment 1 (r/AskReddit)

Be structured, specific, and avoid speculation.

---

🗂 Reddit Activity:
{combined_text}
"""

    return prompt


def generate_persona_with_ollama(username, posts, comments, model = "tinyllama"):
    prompt = generate_prompt(username, posts, comments)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task("⏳ Generating persona with Mistral (optimized)...", start=False)
        progress.start_task(task)

        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

    persona = response['message']['content']
    console.print("[green]✅ Persona generated successfully![/green]")
    return persona
