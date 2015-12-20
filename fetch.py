#!/usr/bin/env python3
"""
Requirements:

requests (installation: pip install requests)
"""
from collections import OrderedDict
import requests
import json
import sys

prompt = """
The script fetches data from http://jsonplaceholder.typicode.com/posts/<user_id>
input user_id, it has to be an integer (0 < user_id <= 100): 
"""

print(prompt)
TYPICODE_URL = 'http://jsonplaceholder.typicode.com/posts/'

while True:
    try:
        user_id = int(input())
        fetch_url = TYPICODE_URL + str(user_id)
        resp = requests.get(url=fetch_url)
    except ValueError:
        print('user_id has to be a number')
    except requests.exceptions.RequestException:
        print('It looks like you have problems with your network. Check it and try again later')
        sys.exit(1)
    else:
        if 0 < user_id <= 100:
            break
        else:
            print('Please, provide correct data (0 < user_id <= 100)')



data = json.loads(resp.text, object_pairs_hook=OrderedDict)
print()
for key, value in data.items():
    print("{}: {}".format(key, value))
