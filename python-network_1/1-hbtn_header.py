#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the value of X-Request_Id
"""
import sys
import requests

def main():
    url = sys.argv[1]
    res = requests.get(url)

    try:
        x_request_id = res.headers['X-Request-Id']
        if x_request_id:
            print(x_request_id)
        else:
            print("None")
    except requests.exceptions.ConnectionError as e:
        print("Connection Error:", e)
    except requests.exceptions.MaxRetryError as e:
        print("Max Retry Error:", e)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
