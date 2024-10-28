import requests
import json
import time


def fetch_comments(subreddit, limit=100, max_comments=1000):
    url = "https://api.pushshift.io/reddit/comment/search/"
    all_comments = []
    params = {
        "subreddit": subreddit,
        "sort": "asc",
        "size": limit
    }
    count = 0
    last_comment_time = None

    while count < max_comments:
        if last_comment_time:
            params['after'] = last_comment_time

        response = requests.get(url, params=params)
        if response.status_code != 200:
            print("Error:", response.status_code)
            break

        data = response.json().get("data", [])

        if not data:
            print("No more comments found.")
            break

        for comment in data:
            all_comments.append(comment)
            count += 1
            last_comment_time = comment["created_utc"]

            if count >= max_comments:
                break

        time.sleep(1)

    return all_comments


def save_comments_to_json(comments, filename="comments.json"):
    with open(filename, "w") as f:
        json.dump(comments, f, indent=4)
    print(f"Saved {len(comments)} comments to {filename}")


subreddit_name = "subreddit_of_your_choice"
max_comments = 500

# Fetch and save comments
comments = fetch_comments(subreddit_name, max_comments=max_comments)
save_comments_to_json(comments, filename=f"{subreddit_name}_comments.json")
