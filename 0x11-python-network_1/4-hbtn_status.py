#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    # make the request and get the response
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    # extract the body content from the response
    content = response.text

    # print the body content with formatting
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(content), content))
