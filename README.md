#  Reddit Persona Analyzer

**Generate psychological user personas from Reddit activity using LLMs like TinyLlama, Mistral (via Ollama), or OpenAI.**

---

##  Overview

This tool scrapes a Reddit user's **recent posts and comments** and uses a language model to generate a **structured psychological persona** that includes:

-  Interests  
-  Writing Style  
-  Personality Traits  
-  Opinions or Beliefs  
-  Demographic Clues (if implied)  
-  With proper post/comment citations

---

##  Features

-  Scrapes Reddit posts & comments using `praw`
-  Generates personas using:
  - `Ollama` (TinyLlama, Mistral, etc.)
  - or `OpenAI GPT models`
-  Command-line interface using `argparse`
-  Saves persona reports to `output/` folder
-  Logs all activity to `logs/app.log`
-  Modular and production-ready

---

##  Installation

```bash
git clone https://github.com/Bharatmallipuram/reddit-persona-analyzer.git
cd reddit-persona-analyzer
python -m venv venv
venv\Scripts\activate        # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
```

## Environment Setup
Create a .env file from the provided template:
```bash
# .env.template → rename to .env
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
USER_AGENT=reddit-persona-analyzer/0.1
```

## Usage
```bash
# Basic usage with TinyLlama (via Ollama)
python src/main.py --username kojied --model tinyllama

# Use mistral instead (if pulled)
python src/main.py --username exampleuser --model mistral
```
Output will be saved to the output/ folder as a .txt file.

## Project Structure
```bash
reddit-persona-analyzer/
├── .env.template
├── requirements.txt
├── README.md
├── logger.py
├── output/
├── logs/
├── src/
│   ├── main.py
│   ├── persona_generator.py
│   ├── reddit_scraper.py
│   └── utils.py
```

## Sample Output
kojied_persona.txt
```bash
Interests:
- Philosophy, AI, and technology ↳ Source: Post 1 (r/singularity)
- Self-reflection and motivation ↳ Source: Comment 2 (r/DecidingToBeBetter)

Writing Style:
- Thoughtful and articulate
- Frequently uses analogies and reflective tone
...
```

## Tech Stack

 Python 3.10+
 PRAW (Reddit API wrapper)
 Ollama (TinyLlama, Mistral)
 argparse + dotenv + logging
 rich for beautiful terminal outputs

## Author
Bharat Mallipuram
AI & LLM Enthusiast | Full-Stack Dev
[Github_link](https://github.com/Bharatmallipuram)

## License
This project is for educational and assignment purposes only.
```markdown

Let me know if you'd like a **compressed summary**, **OpenAI mode added**, or even a **badge-style header for GitHub**.
```