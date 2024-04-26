#!/usr/bin/python3
"""script to query github api"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    creds = {"username": username, "password": password}
    req = requests.post(url, data=creds)
    if req.status_code == 200:
        data = req.json()
        print(data["id"])
    else:
        print("Failed to retrieve GitHub id. Error code:", response.status_code)
