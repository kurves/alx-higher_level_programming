#!/usr/bin/python3
"""script to query github api"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    creds =  HTTPBasicAuth(username, password)
    req = requests.get(url, auth=creds)
    if req.status_code == 200:
        data = req.json()
        print(data["id"])
    else:
        print("None")
