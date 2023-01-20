#!/usr/bin/python3

"""Gets a website using urllib"""
import urllib.request

if __name__ == "__main__":
    req = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(req) as res:
        h = res.read()
        print("Body response:\n"
                "\t- type: {}\n"
                "\t- content: {}\n"
                "\t- utf8 content: {}".format(type(h), h, h.decode("utf-8")))
