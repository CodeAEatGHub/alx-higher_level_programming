#!/usr/bin/python3
"""Displays the response from a url"""

import urllib.request
import sys

if __name__ == "__main__":
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: ", error.code)
