import requests
import json
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import time

# Constants
SUBREDDIT = 'python'
BASE_URL = "https://api.pushshift.io/reddit/comment/search/"
MAX_COMMENTS = 500
CHUNK_SIZE = 100
OUTPUT_FILE = "reddit_comments.json"


def fetch_comments(before=None):
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
        print(f"Failed to fetch comments: Status {response.status_code}")
        return []


def download_comments_threadpool():
    comments = []
    before = None

    with ThreadPoolExecutor() as executor:
        futures = []

        for _ in range(MAX_COMMENTS // CHUNK_SIZE):
            futures.append(executor.submit(fetch_comments, before))
            if comments:
                before = comments[-1]["created_utc"]

        for future in as_completed(futures):
            comments.extend(future.result())
            if len(comments) >= MAX_COMMENTS:
                break

    comments.sort(key=lambda x: x["created_utc"])
    with open("reddit_comments_threadpool.json", "w") as f:
        json.dump(comments, f, indent=4)
    print(f"Downloaded {len(comments)} comments using ThreadPoolExecutor")


def download_comments_processpool():
    comments = []
    before = None

    with ProcessPoolExecutor() as executor:
        futures = []

        for _ in range(MAX_COMMENTS // CHUNK_SIZE):
            futures.append(executor.submit(fetch_comments, before))
            if comments:
                before = comments[-1]["created_utc"]

        for future in as_completed(futures):
            comments.extend(future.result())
            if len(comments) >= MAX_COMMENTS:
                break

    comments.sort(key=lambda x: x["created_utc"])
    with open("reddit_comments_processpool.json", "w") as f:
        json.dump(comments, f, indent=4)
    print(f"Downloaded {len(comments)} comments using ProcessPoolExecutor")


if __name__ == "__main__":
    start = time.time()
    download_comments_threadpool()
    threadpool_time = time.time() - start
    print(f"ThreadPoolExecutor took {threadpool_time:.4f} seconds")

    start = time.time()
    download_comments_processpool()
    processpool_time = time.time() - start
    print(f"ProcessPoolExecutor took {processpool_time:.4f} seconds")
