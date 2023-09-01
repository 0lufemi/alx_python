#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the value of X-Request_Id
"""
import sys
import requests

def main():
    url = sys.argv[1]

    try:
        res = requests.get(url)
        x_request_id = res.headers['X-Request-Id']
        res.raise_for_status()

        if x_request_id:
            print(x_request_id)
        else:
            return None
    # except requests.exceptions.ConnectionError as e:
    #     print("Connection Error:", e)
    #     sys.exit(1)
    # except requests.exceptions.MaxRetryError as e:
    #     print("Max Retry Error:", e)
    #     sys.exit(1)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        sys.exit(1)

    # except requests.exceptions.HTTPError as e:
    #     print(f"Error code: {e.res.status_code}")
    #     sys.exit(1)

if __name__ == "__main__":
    main()
