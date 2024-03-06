#!/usr/bin/python3
"""
Script querying reddit API
"""
import json
import requests
import sys


def count_words(subreddit, word_list, query=None):
    """ Queries the first 10 hot posts of a subreddit """

    hot_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    hot_list = []
    header = {'User-Agent': "Apache helicopter"}

    if (query is not None):
        hot_posts = requests.get(hot_url, params=query, headers=header)
    else:
        hot_posts = requests.get(hot_url, headers=header)

    if (hot_posts.status_code == 200):
        h_posts = json.loads(hot_posts.text).get('data')

        q_string = h_posts.get('after')
        if (q_string):
            params = {
                'count': 25,
                'after': q_string
            }
            recurse_qstring = count_words(subreddit, word_list, query=params)
            if (recurse_qstring is not None):
                [hot_list.append(x) for x in recurse_qstring]

        for post in h_posts.get('children'):
            hot_list.append(post.get('data').get('title'))

        if (h_posts.get('before') is None):
            d_word_list = dict.fromkeys(
                sorted([x.lower() for x in word_list]), 0)
            for hot in hot_list:
                for word in word_list:
                    if word in hot:
                        d_word_list[word] += hot.split().count(word)

            new_dict = {}
            for label, count in d_word_list.items():
                if count == 0:
                    continue
                x = str(count)
                new_dict[x] = new_dict[x].append(
                    label) if new_dict.get(x) else [label]

            for count, label in new_dict.items():
                if count == 0:
                    continue
                for name in label:
                    print(f'{name}: {count}')

    return (None if len(hot_list) == 0 else hot_list)


if __name__ == "__main__":
    count_words(sys.argv[1])
