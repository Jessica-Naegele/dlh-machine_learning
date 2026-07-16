#!/usr/bin/env python3
"""
--- TASK 4 ---
script displaying number of launches per rocket
"""

import requests

if __name__ == '__main__':
    """all launches
    rocket name and number of launches seperated by :
    order result by number of launches desc
    if # launches same --> name abc """

    url = "https://api.spacexdata.com/v4/launches"
    response = requests.get(url).json()

    # 2 loops, 1 for rocket id, 2 for how many launches
    frequency = {}
    for launches in response:
        rocket_id = launches.get('rocket')
        if frequency[rocket_id]:
            frequency[rocket_id] = +1
        else:
            frequency[rocket_id] = 0
    
    # map rocket_id
    rockets_url = "https://api.spacexdata.com/v4/rockets"
    rock_resp = requests.get(rockets_url).json()
    rockets = {}

    for rocket in rock_resp:
        for id in list(frequency.keys()):
            if rocket['id'] == id:
                rockets[id] = rocket['name']
    
    result = {}
    for id in list(frequency.keys()):
        result[rocket[id]] = frequency[id]
    
    # sort 1 by keys than by values
    sorted = dict(sorted(sorted(result.items(), key=lambda item: item[0]), key=lambda item: item[1], reverse=True))

    print(sorted)
