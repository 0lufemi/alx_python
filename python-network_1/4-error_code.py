#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response.
"""

import sys
import requests

def main():
    url = sys.argv[1]

    try:
        res = requests.get(url)
        res.raise_for_status()

        if res.status_code >= 400:
            print(f"Error code: {res.status_code}")
        # else:
        #     print(f"Error code: {res.status_code}")
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
