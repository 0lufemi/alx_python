#!/usr/bin/python3
"""
Use requests package to make a post request to given URL with argument
set in variable `q`, defaulting to empty string. If response body is properly
JSON formatted and not empty, display `id` and `name` as given format.
Otherwise display error message.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    payload = {'q': arg}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=payload)
    try:
        response.raise_for_status()
        response_json = response.json()
        if len(response_json) == 0:
            print("No result")
        else:
            print(f"[{response_json['id']}] {json['name']}")
    except Exception:
        print("Not a valid JSON")
