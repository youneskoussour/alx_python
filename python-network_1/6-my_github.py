#!/usr/bin/python3
"""A Python script that takes your
GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import requests
import sys

def main():
    """The method use to get my GitHub credentials
    (username and password)"""
    if len(sys.argv) != 3:
        print("Usage: python 6-my_github.py youneskoussour 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")
        return
    username = sys.argv[1]
    token = sys.argv[2]

    url = f"https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    
    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])

    else:
        print("None")

if __name__ == "__main__":
    main()