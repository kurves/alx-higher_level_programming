#!/usr/bin/python3
"""fetching data using urllibi and returning header var"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        request_id = res.headers.get('X-Request-Id')
        print(request_id)
