#!/usr/bin/env python3
""" TASK 0
method returning list of ships 
"""

import requests


def availableShips(passengerCount):
    """
    method returning list of ships 
    attr:
    - given number of passengers which needs to be hold
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    with requests.Session() as s:
        
        while url:
            r = requests.get(url).json()
            for ship in r.get('results', []):
                prassenger_str = ship['passengers']
                prassenger_str = prassenger_str.replace(',', '')
                prassenger_str = prassenger_str.replace('n/a', '0')
                prassenger_str = prassenger_str.replace('unknown', '0')
                # print(f"passengers {prassenger_str}")
                if int(prassenger_str) >= int(passengerCount):
                    ships.append(ship["name"])
                # print(f"ship: {ship["passengers"]}")
                # print(f"r[3:]: {r[3:]}")
            next = r.get('next')
            url = next
        # print(f"next:  {r.get('next')}")
    
    return ships
