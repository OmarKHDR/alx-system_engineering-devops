#!/usr/bin/python3
"""First script that uses Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """A function to do stuff that can be done using other functions"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    user_agent = "frog-in-well"
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    res = requests.get(url, headers=headers, allow_redirects=False)
    dic = res.json()
    if res.status_code >= 400:
        return 0
    else:
        return dic['data']['subscribers']

