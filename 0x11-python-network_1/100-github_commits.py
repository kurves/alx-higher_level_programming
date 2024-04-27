#!/usr/bin/python3
"""script to query github api"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    repo = sys.argv[1]
    username = sys.argv[2]
    url = "https://developer.github.com/v3/repos/commits/"
    creds = HTTPBasicAuth(repo, username)
    req = requests.get(url, auth=creds)
    if req.status_code == 200:
        data = req.json()
        print(data["commit"])
    else:
        print("None")


