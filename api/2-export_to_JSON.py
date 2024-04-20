#!/usr/bin/python3
"""RESTful API for employee"""

import json
import requests
import sys


def get_employee_tasks(employee_id):

    employee_name = ""
    task_data = {"USER_ID": []}

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    task_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    if isinstance(user_data, list):
        user_data = user_data[0]

    employee_name = user_data.get('name')

    tasks_response = requests.get(task_url)
    tasks_data = tasks_response.json()

    for task in tasks_data:
        task_data["USER_ID"].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_name
        })

    filename = f"{employee_id}.json"
    with open(filename, 'w') as jsonfile:
        json.dump(task_data, jsonfile, indent=4)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_tasks(employee_id)
