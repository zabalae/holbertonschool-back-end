#!/usr/bin/python3
"""RESTful API for employee"""
import csv
import requests
from sys import argv


if __name__ == "__main__":

    user_id = argv[1]

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + user_id).json()
    NAME = user_url.get('username')
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + user_id + '/todos')
    with open("{}.csv".format(user_id), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in todos.json():
            writer.writerow([user_id, NAME, x.get('completed'),
                             x.get('title')])
