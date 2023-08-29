"""
Python script that takes in a URL, sends a request to the URL and displays the value of X-Request_Id
"""
import sys
import requests

url = sys.argv[1]

res = requests.get(url)
if __name__ == "__main__":
    print(res.headers['X-Request-Id'])
