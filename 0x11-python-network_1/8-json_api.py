#!/usr/bin/python3
"""script to query data"""

import sys
import requests
if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    letter = {"q": q}
    req = requests.post(url, data=letter)
    try:
        data = req.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
