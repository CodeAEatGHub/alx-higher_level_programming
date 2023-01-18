#!/usr/bin/python3
"""Displays error code"""

if __name__ == "__main__":
    import requests
    import sys
    url = sys.argv[1]
    res = requests.get(url)
    if res.status_code != requests.codes.ok:
        print('Error code: {}'.format(response.status_code))
    else:
        print(res.text)
