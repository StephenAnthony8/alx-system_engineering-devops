#!/usr/bin/python3
"""
Script querying reddit API
"""
import json
import requests
import sys


def recurse(subreddit, hot_list=[], query=''):
    """ Queries the first 10 hot posts of a subreddit """

    hot_url = f"https://www.reddit.com/r/{subreddit}/hot.json{query}"

    hot_posts = requests.get(hot_url)

    if (hot_posts.status_code == 200):
        h_posts = json.loads(hot_posts.text).get('data')

        q_string = h_posts.get('after')
        if (q_string):
            recurse_qstring = recurse(subreddit, query=f"?after={q_string}")
            if (recurse_qstring is not None):
                [hot_list.append(x) for x in recurse_qstring]

        for post in h_posts.get('children'):
            hot_list.append(post.get('data').get('title'))

    return (None if len(hot_list) == 0 else hot_list)


if __name__ == "__main__":
    recurse(sys.argv[1])
