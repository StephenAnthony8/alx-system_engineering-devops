#!/usr/bin/python3
"""
Script querying reddit API
"""
import json
import requests
import sys


def top_ten(subreddit):
    """ Queries the first 10 hot posts of a subreddit """

    hot_url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    hot_posts = requests.get(hot_url)

    if (hot_posts.status_code == 200):
        try:
            h_posts = json.loads(hot_posts.text).get('data').get('children')

            for post in h_posts:
                print(post.get('data').get('title'))
        except Exception:
            print(None)
    else:
        print(None)


if __name__ == "__main__":
    top_ten(sys.argv[1])
