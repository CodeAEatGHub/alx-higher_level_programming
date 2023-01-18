#!/usr/bin/python3
"""POSTS url email"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    d = {'email': email}
    res = requests.post(url, data=d)
    print(res.text)
