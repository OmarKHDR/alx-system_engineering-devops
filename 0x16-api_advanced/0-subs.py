#!/usr/bin/python3
""" 1docs docs """
import requests


def number_of_subscribers(subreddit):
    """ pls accept """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'frog-in-well'
    }
    res = requests.get(url, headers)
    if res.status_code != 200:
        return 0
    else:
        try:
            return res.json()['data']['subscribers']
        except:
            pass
    return 0
