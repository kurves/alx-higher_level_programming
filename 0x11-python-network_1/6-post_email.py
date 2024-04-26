#!/usr/bin/python3
"""sending data  data using requesys and returning the body res"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = requests.urlencode({'email': email}).encode()
    req = requests.post(url, data=data)
    body = req.text
    print(body.decode('utf-8'))
