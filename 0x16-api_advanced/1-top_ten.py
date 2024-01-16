#!/usr/bin/python3
"""Function to print hot posts on given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 404:
            print("None")
            return

        results = response.json().get("data", {}).get("children", [])

        for child in results:
            title = child.get("data", {}).get("title")
            print(title)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print("None")

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
