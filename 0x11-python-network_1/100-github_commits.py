#!/usr/bin/python3
""" Script to list 10 commits from repository 'rails' and user 'rails' """
import requests
from sys import argv

#
if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
          .format(argv[2], argv[1])

    response = requests.get(url)
    n = 0

    for i in response.json():
        if n < 10:
            print("{}: {}".format(i.get("sha"),
                  i.get("commit").get("author").get("name")))
        n += 1
