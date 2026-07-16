#!/usr/bin/env python3
"""
This module displays the first launch.
"""
import requests


if __name__ == '__main__':
    """
    Displays the first launch with these information:
       Name of the launch
       The date (in local time)
       The rocket name
       The name (with the locality) of the launchpad.
    """
    launch_url = "https://api.spacexdata.com/v4/launches"
    with requests.get(launch_url) as r_launch:
        # print("Status Code:", r_launch.status_code)
        # print("Raw Response Text:", r_launch.text)
        launches = r_launch.json()
        # print(r_launch.headers.get('Content-Type'))  --> ohne text
        print(f"r_launch: {r_launch}")

        first_launch = min(launches, key=lambda launch: launch["date_unix"])

        launch_name = first_launch.get('name')
        launch_date = first_launch.get('date_local')
        id_rocket = first_launch.get('rocket')
        id_launchpad = first_launch.get('launchpad')

        # decode ROCKET

        rocket_url = "https://api.spacexdata.com/v4/rockets"
        r_rocket = requests.get(rocket_url)
        rocket_json = r_rocket.json()
        rocket_name = rocket_json.get('name')

        # decode launchpad
        lp_url = "https://api.spacexdata.com/v4/launchpads"
        r_lp = requests.get(lp_url)
        lp_json = r_lp.json()
        lp_name = lp_json.get('name')
        lp_locality = lp_json.get('locality')

        # <launch name> (<date>) <rocket name> -
        # <launchpad name> (<launchpad locality>)
        print(f"{launch_name} ({launch_date}) "
              "{rocket_name} - {lp_name} ({lp_locality})")
