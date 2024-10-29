import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

SUBREDDIT = 'python'
BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
MAX_COMMENTS = 500
CHUNK_SIZE = 100
OUTPUT_FILE = "reddit_comments.json"


def fetch_comments(before):
    params = {
        "subreddit": SUBREDDIT,
        "size": CHUNK_SIZE,
        "before": before,
        "sort": "desc"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("data", [])
    else:
        print(f"Failed to fetch comments: {response.status_code}")
        return []


def download_comments():
    comments = []
    before = None

    with ThreadPoolExecutor() as executor:
        futures = []

        for _ in range(MAX_COMMENTS // CHUNK_SIZE):
            future = executor.submit(fetch_comments, before)
            futures.append(future)
            if comments:
                before = comments[-1]["created_utc"]

        for future in as_completed(futures):
            result = future.result()
            comments.extend(result)
            if len(comments) >= MAX_COMMENTS:
                break

    comments.sort(key=lambda x: x["created_utc"])

    with open(OUTPUT_FILE, "w") as f:
        json.dump(comments, f, indent=4)

    print(f"Downloaded {len(comments)} comments from r/{SUBREDDIT} and saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    download_comments()
