import praw
import os
from dotenv import load_dotenv

load_dotenv()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("USER_AGENT")
    )

def is_valid_text(text, min_length=50):
    if not text:
        return False
    text = text.strip()
    return len(text) >= min_length and text.lower() not in ["[deleted]", "[removed]"]

def scrape_user_data(username, limit=100):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    comments = []

    # Fetch posts
    try:
        for submission in user.submissions.new(limit=limit):
            if is_valid_text(submission.selftext):
                posts.append({
                    "title": submission.title,
                    "selftext": submission.selftext,
                    "subreddit": str(submission.subreddit),
                    "url": submission.url,
                    "created_utc": submission.created_utc,
                    "permalink": submission.permalink
                })
    except Exception as e:
        print(f"[!] Error fetching posts for {username}: {e}")

    # Fetch comments
    try:
        for comment in user.comments.new(limit=limit):
            if is_valid_text(comment.body):
                comments.append({
                    "body": comment.body,
                    "subreddit": str(comment.subreddit),
                    "link_title": comment.link_title,
                    "created_utc": comment.created_utc,
                    "permalink": comment.permalink
                })
    except Exception as e:
        print(f"[!] Error fetching comments for {username}: {e}")

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }

# Test run
if __name__ == "__main__":
    username = "Hungry-Move-6603"
    data = scrape_user_data(username)

    print(f"\n🔍 Found {len(data['posts'])} filtered posts and {len(data['comments'])} filtered comments for {username}")
    print("Sample post:", data["posts"][0]["title"] if data["posts"] else "No posts")
    print("Sample comment:", data["comments"][0]["body"] if data["comments"] else "No comments")
