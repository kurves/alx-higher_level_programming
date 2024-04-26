#!/usr/bin/python3
"""fetching data using urllib"""

import urllib.request

req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as res:
    data = res.read()
    print(data)
