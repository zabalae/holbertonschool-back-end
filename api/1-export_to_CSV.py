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
    f_name = u_id + '.csv'
    with open(f_name, 'w', encoding='utf-8') as f:
        for info in todos:
            TASK_COMPLETED_STATUS = info.get("completed")
            TASK_TITLE = info.get("title")
            f.write('"{}","{}","{}","{}"\n'.format(
                u_id, NAME, TASK_COMPLETED_STATUS, TASK_TITLE))


if __name__ == "__main__":
    csv_format()
