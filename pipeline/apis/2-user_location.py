#!/usr/bin/env python3
"""--- TASK 2 ---
writing a script that prints location of a specific user
"""

import requests
from sys import argv
import time

if __name__ == '__main__':
    url = argv[1]
    # print(url)  # helferlein

    # start request
    with requests.get(url) as r:
        if r.status_code == 403:
            ratelimit = int(r.headers.get('X-Ratelimit-Reset', 0))
            current_timestamp = int(time.time())
            x = int(round((ratelimit - current_timestamp) / 60))
            print(f"reset in {x} min")
        elif r.status_code == 404:
            print("Not found")
        else:
            r_text = r.json()
            location = r_text.get('location')
            print(location)
