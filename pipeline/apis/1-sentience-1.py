#!/usr/bin/env python3
"""Module to find home planets of sentient species using SWAPI."""
import requests


def sentientPlanets():
    """Retrieve unique names of home planets of all sentient species.

    Returns:
        list: Unique names of planets.
    """
    url = "https://swapi-api.hbtn.io/api/species/"
    planets = []
    planet_cache = {}

    while url:
        response = requests.get(url).json()
        for species in response.get('results', []):
            classif = species.get('classification') or ''
            desig = species.get('designation') or ''

            if 'sentient' in classif.lower() or 'sentient' in desig.lower():
                homeworld_url = species.get('homeworld')
                if not homeworld_url:
                    planet_name = "unknown"
                else:
                    if homeworld_url in planet_cache:
                        planet_name = planet_cache[homeworld_url]
                    else:
                        p_res = requests.get(homeworld_url).json()
                        planet_name = p_res.get('name', 'unknown')
                        planet_cache[homeworld_url] = planet_name

                if planet_name not in planets:
                    planets.append(planet_name)
        url = response.get('next')

    return planets