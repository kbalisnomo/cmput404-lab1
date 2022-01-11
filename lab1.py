import requests

# What version is the requests library installed on the system?
print("Requests version: " + requests.__version__)

# GET the Google homepage
homepage = requests.get("http://google.com/")
print("GET Google homepage: " + str(homepage.status_code))

# GET this script from GitHub
script = requests.get("https://raw.githubusercontent.com/kbalisnomo/cmput404-lab1/main/lab1.py")
print("GET this script off GitHub:\n", script.text)