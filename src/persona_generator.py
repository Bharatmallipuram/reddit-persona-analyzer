from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
import ollama
from utils import clean_text, format_for_citation

console = Console()

def generate_prompt(username, posts, comments):
    combined_text = ""

    for i, post in enumerate(posts[:3]):
        text = clean_text(post['selftext'], max_length=300)
        citation = format_for_citation(post, i, item_type="Post")
        combined_text += (
            f"\n[Post {i+1} - r/{post['subreddit']}]\n"
            f"Title: {post['title']}\n{text}\n{citation}\n"
        )

    for i, comment in enumerate(comments[:2]):
        text = clean_text(comment['body'], max_length=300)
        citation = format_for_citation(comment, i, item_type="Comment")
        combined_text += (
            f"\n[Comment {i+1} - r/{comment['subreddit']}]\n{text}\n{citation}\n"
        )

    prompt = f"""
You are a professional psychological analyst studying the digital behavior of Reddit users. You will analyze a Reddit user's posts and comments and create a comprehensive, evidence-based psychological persona using only the Reddit data provided.

🔍 Follow this structure:

---

**Top Interests**  
Identify specific domains the user is passionate about based on their Reddit activity (e.g., startup culture, immigration, mental health). Use examples from their posts/comments with clear subreddit citations.  

↳ Format:  
- <interest area>  
↳ Source: Post <#> (r/<subreddit>)  

---

**Communication Style**  
Describe the user's tone, emotional expression, or stylistic tendencies (e.g., storytelling, sarcasm, emojis, directness). Support this with example citations from posts or comments.

↳ Format:  
"<Quote or pattern>"  
↳ Source: Comment <#> (r/<subreddit>)

---

**Personality Traits**  
Infer strong social, political, ethical, or emotional traits. Stick to clearly stated or strongly implied content only. Avoid speculation. Traits could include: introverted, opinionated, anxious, empathetic, confident, etc.

↳ Format:  
- Trait: <description>  
↳ Source: Post/Comment <#> (r/<subreddit>)

---

**Stated Opinions / Beliefs**  
List explicitly stated opinions or beliefs around culture, society, politics, morality, etc., and quote or summarize the statement with citation.

↳ Format:  
"<Belief summary or quote>"  
↳ Source: Post/Comment <#> (r/<subreddit>)

---

**Demographic Clues**  
Summarize any life-stage, geographic, profession, or social identity hints clearly implied by Reddit content. Avoid guessing. Cite where possible.

↳ Format:  
"<Clue summary>"  
↳ Source: Post/Comment <#> (r/<subreddit>)

---

**Confidence Score**  
Rate your overall confidence in the persona on a scale from 1–5 based on the number of posts and comments analyzed.


---

🧠 Be factual, human-like, and to the point. No fluff. Use clean markdown and be concise but insightful.


Reddit Activity to Analyze:
{combined_text}

"""

    return prompt

def calculate_confidence_score(posts, comments):
    count = len(posts) + len(comments)
    score = min(5, count // 10)
    moons = score + (5 - score)
    return f"Confidence Score: {moons} ({score}/5) — based on {len(posts)} posts and {len(comments)} comments."

def generate_persona_with_ollama(username, posts, comments, model="tinyllama"):
    prompt = generate_prompt(username, posts, comments)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        task = progress.add_task(f" Generating persona with {model}...", start=False)
        progress.start_task(task)

        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

    persona = response['message']['content']
    confidence = calculate_confidence_score(posts, comments)
    full_output = f"{persona}\n\n{confidence}"

    console.print("[bold green] Persona generated successfully![/bold green]")
    return full_output
