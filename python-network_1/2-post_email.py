#!/usr/bin/python3
"""
Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as parameter
"""

import requests
import sys

def main():
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(f"Email: {email}")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
