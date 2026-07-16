#!/usr/bin/env python3
"""
TASK 1
method reurning list of names of home planets with sentience
"""

import requests


def sentientPlanets():
    """
    returning list of planets of sentient species
    - sentient type is either in classification or deisgnation
    - looking at sentient species
    """
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []

    with requests.Session() as s:

        while url:
            r = requests.get(url).json()
            for species in r.get('results', []):
                if (
                    species['classification'] == 'sentient'
                    or species['designation'] == 'sentient'
                ):
                    planet_url = species['homeworld']
                    # print(f"homeworld_url: {planet_url}") # helferlein
                    if planet_url is not None:
                        # print(planet_url)
                        p = requests.get(planet_url).json()
                        # print(p)
                        planet = p['name']
                        if planet not in planets:
                            planets.append(planet)
            next = r.get('next')
            url = next
        # print(f"planets:  {planets}")
    return planets
