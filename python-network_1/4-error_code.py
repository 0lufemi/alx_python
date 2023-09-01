#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the body of the response.
"""

import sys
import requests

def main():
    # url = sys.argv[1]

    # try:
    #     res = requests.get(url)
    #     res.raise_for_status()

    #     if res.status_code >= 400:
    #         print(f"Error code: {res.status_code}")
    #     # else:
    #     #     print(f"Error code: {res.status_code}")
    # except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
    #     print(f"An error occurred: {e}")

    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes

        # If the request is successful, print the response body
        print(response.text)
    except requests.exceptions.RequestException as e:
        # Handle any request-related exceptions
        print(f"An error occurred: {e}")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors (4xx and 5xx status codes)
        print(f"Error code: {e.response.status_code}")
        sys.exit(1)



if __name__ == "__main__":
    main()
