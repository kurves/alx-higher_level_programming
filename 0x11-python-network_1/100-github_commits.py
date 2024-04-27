#!/bin/bash/python3
"""script to query github api"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if name = '__main__':
    sys.argv[1] = repo
    sys.argv[2] = username
    url = "https://developer.github.com/v3/repos/commits/"
    creds = (repo, username)
    req = requests.get(url, auth=creds)
    if req.status_code == 200:
        data = req.json()
        print(data["commit])
    else:
        print("None")


