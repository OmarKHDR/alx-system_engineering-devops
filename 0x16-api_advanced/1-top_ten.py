#!/usr/bin/python3
"""Second script that uses Reddit API"""
import requests


def top_ten(subreddit):
    """ |pls |accepted"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'frog-in-well'
    }
    res = requests.get(url, headers, allow_redirects=False)
    if res.status_code != 200:
        print('None')
    else:
        try:
            res = res.json()
            i = 0
            j = 0
            while (i < 10):
                if res['data']['children'][i+j]['data']['selftext'] == "":
                    j += 1
                    continue
                print(res['data']['children'][i+j]['data']['selftext'] )
                i += 1
        except:
            print('None')
