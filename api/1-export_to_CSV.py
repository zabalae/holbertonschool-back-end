#!/usr/bin/python3
'''Export data in the CSV format'''

import csv
import requests
import sys


def csv_format():

    u_id = sys.argv[1]

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + u_id).json()
    NAME = user_url.get('username')
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + u_id + '/todos')
    with open("{}.csv".format(u_id), 'r') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for x in todos.json():
            writer.writerow([u_id, NAME, x.get('completed'), x.get('title')])


if __name__ == "__main__":
    csv_format()
