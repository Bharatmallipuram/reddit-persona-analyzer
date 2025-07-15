import praw
import os
from dotenv import load_dotenv
from logger import setup_logger

load_dotenv()
logger = setup_logger()

def get_reddit_instance():
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        username=os.getenv("REDDIT_USERNAME"),
        password=os.getenv("REDDIT_PASSWORD"),
        user_agent=os.getenv("USER_AGENT")
    )

def scrape_user_data(username, limit=100):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)   #  a special PRAW object that represents the user and lets you access their posts, comments, and metadata

    posts = []
    comments = []

    # Fetch submissions (posts)
    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "subreddit": str(submission.subreddit),  # from which jouner the post or comment comes form.
                "url": submission.url,
                "created_utc": submission.created_utc
            })
        logger.info(f" Fetched {len(posts)} posts for user '{username}'")
    except Exception as e:
        logger.warning(f"[!] Error fetching posts for {username}: {e}")

    # Fetch comments
    try:
        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "link_title": comment.link_title,
                "created_utc": comment.created_utc   # a label that tells you exactly when it was made.  (Universal Time Coordinated)
            })
        logger.info(f" Fetched {len(comments)} comments for user '{username}'")
    except Exception as e:
        logger.warning(f"[!] Error fetching comments for {username}: {e}")

    if not posts and not comments:
        logger.error(f" No content found for user '{username}'")
        raise ValueError("No accessible posts or comments found")

    return {
        "username": username,
        "posts": posts,
        "comments": comments
    }


if __name__ == "__main__":
    username = "Hungry-Move-6603"
    data = scrape_user_data(username)

    print(f"\n Found {len(data['posts'])} filtered posts and {len(data['comments'])} filtered comments for {username}")
    print("Sample post:", data["posts"][0]["title"] if data["posts"] else "No posts")
    print("Sample comment:", data["comments"][0]["body"] if data["comments"] else "No comments")
