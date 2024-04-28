#!/usr/bin/python3
"""script to query github api"""
import sys
import requests

if __name__ == "__main__":
        repo = sys.argv[1]
        username = sys.argv[2]
        url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
        req = requests.get(url)
        if req.status_code == 200:
            data = req.json()
            print(data["commit"])
        else:
            print("None")


