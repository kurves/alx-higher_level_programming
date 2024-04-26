#!/usr/bin/python3
"""sending data  data using urllibi and returning the body res"""

import urllib.request
import sys
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode()
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))
