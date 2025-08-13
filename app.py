import requests
import os

API_URL = os.getenv("API_URL")

def fetch_greynoise(ip):
    url = API_URL+ip
    return requests.get(url).json()