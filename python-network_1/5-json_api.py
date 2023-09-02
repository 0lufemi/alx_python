#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

def main():
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    try:
        payload = {"q" : letter}
        r = requests.post(url, data = payload)
        r.raise_for_status()

        r_json = r.json()
        id = r_json["id"]
        name = r_json["name"]

        if len(r_json) != 0:
            print(f"{id} {name}")
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
