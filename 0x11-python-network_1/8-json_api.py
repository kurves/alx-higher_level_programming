#!/usr/bin/python3
"""script to query data"""

import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    letter = sys.argv[2]
    req = requests.post(url, data={'letter': letter})
    body = req.json
    if body.type == json:
        print(body)
    else:
        'Not a valid JSON'
    print(body)
