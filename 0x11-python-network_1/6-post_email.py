#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the passed URL"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    
    resp = requests.post(url, value)
    print(resp.text)
