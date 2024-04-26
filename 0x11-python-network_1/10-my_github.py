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
    try:
        data = req.json()
        if data:
            print("[{}] {}".format(data.get("id"), data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
