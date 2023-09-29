#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value"""
import requests


if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print(resp.headers.get("X-Request-Id"))
