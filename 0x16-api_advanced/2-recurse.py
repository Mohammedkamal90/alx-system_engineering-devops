#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests

def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of titles of all hot posts on a given subreddit.

    Parameters:
        subreddit (str): The subreddit to query.
        hot_list (list): List to store titles of hot posts.
        after (str): Identifier for the last post in the previous request.
        count (int): Number of posts retrieved so far.

    Returns:
        list or None: List of titles if successful, None if subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
