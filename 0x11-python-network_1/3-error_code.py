#!/usr/bin/python3
"""script that displays data in decoded form"""

import urllib.request
import sys
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
