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

def scrape_user_data(username, limit=100):
    reddit = get_reddit_instance()
    user = reddit.redditor(username)

    posts = []
    comments = []

    # Fetch submissions (posts)
    try:
        for submission in user.submissions.new(limit=limit):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext,
                "subreddit": str(submission.subreddit),
                "url": submission.url,
                "created_utc": submission.created_utc
            })
    except Exception as e:
        print(f"[!] Error fetching posts for {username}: {e}")

    # Fetch comments
    try:
        for comment in user.comments.new(limit=limit):
            comments.append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "link_title": comment.link_title,
                "created_utc": comment.created_utc
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
    username = "Hungry-Move-6603"  # You can change this to test other users
    data = scrape_user_data(username)

    print(f"\n🔍 Found {len(data['posts'])} posts and {len(data['comments'])} comments for {username}")
    print("Sample post:", data["posts"][0]["title"] if data["posts"] else "No posts")
    print("Sample comment:", data["comments"][0]["body"] if data["comments"] else "No comments")
