#!/usr/bin/python3
"""Script that displays the X-Request-Id header value for a given URL."""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
