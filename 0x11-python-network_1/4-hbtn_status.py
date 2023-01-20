#!/usr/bin/python3
"""Tests status of web pages"""

import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    res = requests.get(url)
    con = res.text
    print("Body response:"
          "- type: {}"
          "- content: {}".format(type(con), con))
