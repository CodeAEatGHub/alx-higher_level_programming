#!/usr/bin/python3
"""Gets X-Request-Id from a url"""

import urllib.request
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as res:
        print(res.getheader('X-Request-Id'))
