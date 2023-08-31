# Python - Network

## 0. What's my status? #1
Write a Python script that fetches ```https://alu-intranet.hbtn.io/status```
* You must use the package ```requests```
* You are not allow to import packages other than ```requests```
* The body of the response must be display like the following example (tabulation before ```-```)

## 1. Response header value #1
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable ```X-Request-Id``` in the response header
* You must use the packages ```requests``` and ```sys```
* You are not allow to import other packages than ```requests``` and ```sys```
* The value of this variable is different for each request
* You don’t need to check script arguments (number and type)

## 2. POST an email #1
Write a Python script that takes in a URL and an email address, sends a ```POST``` request to the passed URL with the email as a parameter, and finally displays the body of the response.
* The email must be sent in the variable ```email```
* You must use the packages ```requests``` and ```sys```
* You are not allowed to import packages other than ```requests``` and ```sys```
* You don’t need to error check arguments passed to the script (number or type)
Please test your script in the container provided, using the web server running on port 5000
