#!/usr/bin/python3
"""
Script querying reddit API
"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """ Queries the number of subscribers a subreddit has """

    subreddit_url = f"https://www.reddit.com/r/{subreddit}.json"

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0",
        'client_id': '9FJ_bWxq1SY7zOcYkRXBbw'
    }

    subs_count = requests.get(subreddit_url,
                              headers=headers,
                              allow_redirects=False
                              )

    if (subs_count.status_code == 200):
        subs_count = json.loads(subs_count.text)
        r_dict = subs_count.get('data')
        r_child = r_dict.get('children')[0]
        r_data = r_child.get('data')
        r_sub = r_data.get('subreddit_subscribers')

        return (r_sub)
    else:
        return (0)


if __name__ == "__main__":
    print(number_of_subscribers(sys.argv[1]))
