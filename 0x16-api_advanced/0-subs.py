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
    res = requests.get(url, headers=headers, allow_redirects=True)
    try:
        dic = res.json()
    except:
        return 0
    if res.status_code >= 400:
        return 0
    else:
        return dic['data']['subscribers']

import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))