# 🧠 Reddit User Persona Generator (LLM-Powered) – BeyondChats Assignment

This project generates structured user personas from Reddit profiles using a local LLM (TinyLlama). Given any Reddit username, the system scrapes their recent posts/comments and builds a human-like persona with citations using language modeling.


## 🚀 Features

- 🔍 Scrapes Reddit posts and comments via PRAW
- 🤖 Generates concise user personas using a local LLM (TinyLlama via Ollama)
- 📄 Outputs results as clean, structured `.txt` files
- 🧾 Citations included (e.g., Post 1 from r/AskReddit)
- ✅ Modular design – Easily switch to GPT-4, Mistral, or any other model


## 🛠️ Tech Stack

| Purpose          | Tech Used                |
|------------------|--------------------------|
| Reddit Scraping  | `praw`                   |
| Persona Modeling | `TinyLlama` via `Ollama` |
| CLI Interface    | `argparse` + `rich`      |
| Secrets Handling | `python-dotenv`          |
| Output Format    | Plaintext `.txt`         |


## 🧪 Sample Usage

```bash
python src/main.py --url https://www.reddit.com/user/Hungry-Move-6603 --model ollama
```
Output is saved to: output/Hungry-Move-6603_persona.txt

🗃️ Project Structure
```bash
├── src/
│   ├── main.py                  # Entry point
│   ├── persona_generator.py     # Generates persona using Ollama
│   ├── reddit_scraper.py        # Fetches Reddit posts/comments
│   ├── utils.py                 # Text cleaning + citation helpers
├── output/                      # Generated personas
├── .env.template                # Example env vars
├── requirements.txt             # Python dependencies
└── README.md
```

## Environment Variables
Copy .env.template and rename it to .env. Fill in your Reddit credentials:
```bash
Environment Variables
Copy .env.template and rename it to .env. Fill in your Reddit credentials:
```
Ollama will use the TinyLlama model automatically.

## Why TinyLlama?
“I chose TinyLlama to ensure fast, local persona generation on limited hardware (i5-1235U, 8GB RAM). It balances speed and quality, with modularity to swap in Mistral or GPT-4 if required.”

This shows resource-aware engineering — a key skill for real-world AI deployment.

## Model Output Example
``bash
## User Persona: Hungry-Move-6603

### Interests
- Interested in startup culture and tech innovations
↳ Source: Post 1 (r/startups)

### Communication Style
- Informal, humorous, uses emojis
↳ Source: Comment 2 (r/funny)

### Personality Traits
- Curious, helpful, and slightly sarcastic
↳ Source: Post 2 (r/technology)

```

✅ How to Run
Clone this repo

Set up .env

Run:

bash
Copy
Edit

```bash
pip install -r requirements.txt
python src/main.py --url <Reddit Profile URL> --model ollama
```

## Notes
Output files are saved in output/ folder

Only recent 3 posts & 2 comments are analyzed (can be changed)

To switch to OpenAI or other models, plug into the modular interface

## 🙋 About Me
This project was submitted as part of the AI/LLM Engineer Internship Assignment for BeyondChats.
Feel free to explore, suggest, or fork!

Designed for performance, readability, and future extensibility.
