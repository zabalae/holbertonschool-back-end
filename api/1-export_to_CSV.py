#!/usr/bin/python3
'''Export data in the CSV format'''
import requests
import sys


def csv_format():

    id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(id)
    response = requests.get(user_url).json()
    NAME = response.get('username')
    response = requests.get(url).json()
    with open("{}.csv".format(id), 'w') as f:
        for info in response:
            TASK_COMPLETED_STATUS = info.get("completed")
            TASK_TITLE = info.get("title")
            f.write('"{}","{}","{}","{}"\n'.format(
                id, NAME, TASK_COMPLETED_STATUS, TASK_TITLE))


if __name__ == '__main__':
    csv_format()
