#!/usr/bin/env python3
import requests
import sys


def search(keyword):
    after = 'null'
    while (after is not None):
        url = f"https://www.reddit.com/search.json?q={keyword}&after={after}"
        headers = {
            'User-Agent': 'frog-in-well'
        }
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print("error", res.status_code)
            break
        try:
            res = res.json()
            for post in res['data']['children']:
                print(post['data']['title'],":")
                if(post['data']['selftext'] == ""):
                    print("no content")
                else:
                    print(post['data']['selftext'])
                print("\n")
        except:
            print("problem with result")
        after = res['data']['after']

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage ./search query")
        exit(1)
    search(sys.argv[1])
