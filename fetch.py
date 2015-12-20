#!/usr/bin/env python3
"""
Requirements:

requests (installation: pip install requests)
"""
from collections import OrderedDict
import requests
import json

prompt = """
The script fetches data from http://jsonplaceholder.typicode.com/posts/<user_id>
input user_id, it has to be an integer (0 < user_id <= 100): 
"""

print(prompt)

while True:
    try:
        user_id = int(input())
    except ValueError:
        print('user_id has to be a number')
    else:
        if 0 < user_id <= 100:
            break
        else:
            print('Please, provide correct data (0 < user_id <= 100)')

FETCH_URL = 'http://jsonplaceholder.typicode.com/posts/' + str(user_id)

resp = requests.get(url=FETCH_URL)
data = json.loads(resp.text, object_pairs_hook=OrderedDict)
print()
for key, value in data.items():
    print("{}: {}".format(key, value))
