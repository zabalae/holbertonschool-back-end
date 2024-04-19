#!/usr/bin/python3
"""RESTful API for employee"""

import requests
import sys


def get_employee_tasks(employee_id):

    employee_name = ""
    number_of_done_tasks = 0
    total_number_of_tasks = 0
    task_titles = []

    url_users = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/
    /todos?userId={employee_id}"

    user_response = requests.get(url_users)
    user_data = user_response.json()

    if isinstance(user_data, list):
        user_data = user_data[0]

    employee_name = user_data.get('name')

    todos_response = requests.get(url_todos)
    todos_data = todos_response.json()

    for task in todos_data:
        total_number_of_tasks += 1
        if task['completed']:
            number_of_done_tasks += 1
            task_titles.append(task['title'])

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, number_of_done_tasks,
                  total_number_of_tasks))
    for title in task_titles:
        print(f'\t{title}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_tasks(employee_id)
