#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

def main():
    # url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    # try:
    #     payload = {"q" : letter}
    #     r = requests.post(url, data = payload)
    #     r.raise_for_status()

    #     r_json = r.json()
    #     id = r_json["id"]
    #     name = r_json["name"]

    #     if len(r_json) != 0:
    #         print(f"{id} {name}")
    #     else:
    #         print("No result")
    # except Exception:
    #     print("Not a valid JSON")

    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}

    try:
        response = requests.post(url, data=params)
        response_json = response.json()

        if response.status_code == 200:
            if response_json:
                user = response_json[0]
                user_id = user.get('id')
                user_name = user.get('name')
                if user_id is not None and user_name is not None:
                    print(f"[{user_id}] {user_name}")
                else:
                    print("No result")
            else:
                print("No result")
        else:
            print("No result")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
