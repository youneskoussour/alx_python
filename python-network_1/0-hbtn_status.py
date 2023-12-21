"""Python Network Request"""
import requests

req = 'https://alu-intranet.hbtn.io/status'
response = requests.get(req)