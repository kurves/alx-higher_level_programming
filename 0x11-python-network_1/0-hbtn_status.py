#!/usr/bin/python3
"""fetching data using urllib"""

import urllib

req = urrlib.request.Request("https://alx-intranet.hbtn.io/status")
with urllib.request.urlopen(req) as res:
    print(res)
