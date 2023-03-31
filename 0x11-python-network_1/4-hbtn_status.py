#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status """
import requests

if __name__ == "__main__":
    # make the request and get the response
    response = requests.get('https://intranet.hbtn.io/status')

    # extract the body content from the response
    content = response.text

    # print the body content with formatting
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
