#!/usr/bin/python3
"""fetching data using urllib"""

import urllib.request
if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as res:
        data = res.read()
        print("Body response:")
        print("\t- type:", type(data))
        print("\t- content:", data)
        print("\t- utf8 content:", data.decode('utf-8'))
