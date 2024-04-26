#!/usr/bin/python3
"""fetching data using requests module"""

import requests
if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    data = req.text
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
