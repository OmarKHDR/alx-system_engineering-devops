#!/usr/bin/env python3
import requests
import sys
import json
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def print_comments(comment_list: List[Dict[str, Any]], indent: int = 0) -> None:
    if not comment_list:
        logging.info("  " * indent + "No replies")
        return

    for child in comment_list:
        try:
            comment_data = child.get('data', {})
            body = comment_data.get('body', 'No comment body')
            logging.info("  " * indent + body)

            replies = comment_data.get('replies', '')
            if isinstance(replies, dict):
                children = replies.get('data', {}).get('children', [])
                print_comments(children, indent + 1)
            elif replies:
                logging.warning(f"Unexpected 'replies' format: {type(replies)}")
        except Exception as e:
            logging.error(f"Error processing comment: {e}")
            logging.debug(f"Problematic comment data: {json.dumps(child, indent=2)}")

def print_content_and_comments(post: Dict[str, Any], headers: Dict[str, str]) -> None:
    url = f"https://www.reddit.com{post['data']['permalink']}.json"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        body = response.json()
        
        if isinstance(body, list) and len(body) > 1:
            post_data = body[0]['data']['children'][0]['data']
            selftext = post_data.get('selftext', '')
            if selftext:
                logging.info(selftext)
            else:
                logging.info("No text content, can't display media")
            
            comments_data = body[1]['data']
            if 'children' in comments_data:
                print_comments(comments_data['children'])
            else:
                logging.warning("No 'children' found in the comments data")
        else:
            logging.error(f"Unexpected response structure: {json.dumps(body, indent=2)}")
    except requests.RequestException as e:
        logging.error(f"Error fetching post: {e}")
    except Exception as e:
        logging.error(f"Error processing post data: {e}")
        logging.debug(f"Response body: {json.dumps(body, indent=2)}")

def search(keyword: str) -> None:
    after = None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:129.0) Gecko/20100101 Firefox/129.0'
    }

    while True:
        url = f"https://www.reddit.com/search.json?q={keyword}&after={after or ''}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            for post in data['data']['children']:
                logging.info(f"\n{post['data']['title']}:")
                print_content_and_comments(post, headers)

            after = data['data'].get('after')
            if not after:
                break
        except requests.RequestException as e:
            logging.error(f"Error during search: {e}")
            break
        except Exception as e:
            logging.error(f"Error processing search results: {e}")
            logging.debug(f"Response data: {json.dumps(data, indent=2)}")
            break

if __name__ == '__main__':
    if len(sys.argv) != 2:
        logging.error("Usage: ./search.py <query>")
        sys.exit(1)
    search(sys.argv[1])