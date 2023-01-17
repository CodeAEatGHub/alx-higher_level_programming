#!/usr/bin/python3
"""Checks status of web pages"""


if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    response = requests.get(url)
    meta = response.headers
    print(meta.get('X-Request-Id'))