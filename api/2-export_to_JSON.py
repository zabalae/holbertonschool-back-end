#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + user_id).json()
    NAME = user_url.get('username')
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + user_id + '/todos')

    tasks = []
    for task in todos:
        task_dict = {"task": task['title'],
                     "completed": task['completed'],
                     "username": NAME}
        tasks.append(task_dict)
    datas = {user_id: tasks}
    filename = '{}.json'.format(user_id)
    with open(filename, 'w') as f:
        json.dump(datas, f)
