"""Python Network Request"""
import requests

req = 'https://alu-intranet.hbtn.io/status'
response = requests.get(req)

print("Body response:\n\t- type: {}\n\t- content: {}".format(type(response.text), response.text))