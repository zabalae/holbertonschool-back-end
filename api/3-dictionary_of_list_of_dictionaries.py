#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests


if __name__ == "__main__":

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    for user in user_url:
        user_id = user.get('id')
        NAME = user.get('username')
        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId=' + user_id).json()

    datas = {user_id: []}
    for task in tasks:
        task_dict = {"username": NAME,
                     "task": task['title'],
                     "completed": task['completed']}
        datas.get(user_id).append(task_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(datas, f)
