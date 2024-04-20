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

    datas = {user_id: []}
    for task in todos:
        task_dict = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": NAME}
        datas.get(user_id).append(task_dict)
    with open("{}.json".format(user_id), 'w') as f:
        json.dump(datas, f)
