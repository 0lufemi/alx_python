#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the value of X-Request_Id
"""
import sys
import requests

url = sys.argv[1]

res = requests.get(url)
if __name__ == "__main__":
    # try:
    x_request_id = res.headers['X-Request-Id']
    if x_request_id:
        print(x_request_id)
    else:
        print("None")
    # except requests.exceptions.ConnectionError:
    #     print(None)
