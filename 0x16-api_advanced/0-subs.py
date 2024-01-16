#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    """return total number of subscribers on given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        if response.status_code == 404:
            return 0

        results = response.json().get("data")
        subscribers = results.get("subscribers", 0)
        return subscribers

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)

