#!/usr/bin/python3
"""Export data in the JSON format"""
import requests
import json


if __name__ == "__main__":

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    all_employed = {}

    for user in user_url:
        user_id = user.get('id')
        NAME = user.get('username')
        tasks = requests.get(
            f"{user_url}/{user['id']}/todos").json()
        dict_task = [{"username": NAME,
                      "task": task['title'],
                      "completed": task['completed']} for task in tasks]
        all_employed[user_id] = dict_task

    with open('todo_all_employees.json', 'w') as f:
        json.dump(all_employed, f)
