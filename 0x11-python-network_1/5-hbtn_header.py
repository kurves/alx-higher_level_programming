#!/usr/bin/python3
"""fetching data using requests and returning header var"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    request_id = res.headers.get('X-Request-Id')
    print(request_id)
