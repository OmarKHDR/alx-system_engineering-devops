#!/usr/bin/env python3
import requests
import sys


def print_comments(comment_list):
    if comment_list == []:
        print("no replies")
        return
    else:
        for child in comment_list:
            print(child['data']['body'])
            if child['data']['replies'] == "":
                continue
            print_comments(child['data']['replies']['data']['children'])


def print_content_and_comments(post, headers):
    url = f"https://www.reddit.com{post['data']['permalink']}.json"
    body = requests.get(url, headers=headers)
    try:
        body = body.json()
        if body[0]['data']['children'][0]['data']['selftext'] == "":
            print("no text content, cant desplay media")
        else:
            print(body[0]['data']['children'][0]['data']['selftext'])
        print_comments(body[1]['data']['children'])
    except Exception as e:
        print("error in post ", e)


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
                print_content_and_comments(post, headers)
        except Exception as e:
            print("problem with result", e)
        after = res['data']['after']

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage ./search query")
        exit(1)
    search(sys.argv[1])
