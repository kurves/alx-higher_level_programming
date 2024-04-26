#!/usr/bin/python3
"""sending data  data using requesys and returning the body res"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})
    body = req.text
    print(body)
