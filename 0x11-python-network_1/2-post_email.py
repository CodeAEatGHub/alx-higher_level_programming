#!/usr/bin/python3
"""Posts headers"""

import urllib.request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read())
