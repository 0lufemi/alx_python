#!/usr/bin/python3
# """
# Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as parameter
# """
# import requests
# import sys

# url = sys.argv[1]
# email = sys.argv[2]

# payload = {"email": email}
# res = requests.post(url, data= payload)
# if __name__ == "__name__":
#     print(res.text)


import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <URL> <email>")
        return
    
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    
    try:
        response = requests.post(url, data=payload)
        response_body = response.text
        print("Response Body:")
        print(response_body)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
