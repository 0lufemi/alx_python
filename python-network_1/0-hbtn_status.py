"""
Python script that fetches from a url
"""

import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

if __name__ == "__main__":
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
