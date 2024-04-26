#!/usr/bin/python3
"""sending data  data using urllibi and returning the body res"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode(email)
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as req:
        res = req.read()
        print(res.decode('utf-8')
