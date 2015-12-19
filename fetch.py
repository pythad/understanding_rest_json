#!/usr/bin/env python3
"""
Usage:

python3 fetch.py "<user_id>"(0 < user_id <= 100)

Example:

python3 fetch.py 21

Requirements:

requests (installation: pip install requests)
"""

import argparse
import requests
import json

parser = argparse.ArgumentParser(description='Process the query input')
parser.add_argument('user_id', type=int, help='user_id to get data for')
args = parser.parse_args()
user_id = args.user_id

while not 0 < user_id <= 100:
    user_id = int(input("Please, provide correct data (0 < user_id <= 100): "))

FETCH_URL = 'http://jsonplaceholder.typicode.com/posts/' + str(user_id)

resp = requests.get(url=FETCH_URL)
data = json.loads(resp.text)
print('\n')
for key, value in data.items():
    print("{}: {}".format(key, value))
