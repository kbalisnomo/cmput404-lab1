import requests

# What version is the requests library installed on the system?
print("Requests version: " + requests.__version__)

# GET the Google homepage
response = requests.get("http://google.com/")
print("GET Google homepage: " + response.status_code)

