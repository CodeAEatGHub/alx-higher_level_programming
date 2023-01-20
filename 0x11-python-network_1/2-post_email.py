#!/usr/bin/python3
"""Posts headers"""

import urllib.request
import sys

if __name__ == "__main__":
    e = {'email': argv[2]}
    req = requests.post(argv[1], data=e)
    print (req.text)
