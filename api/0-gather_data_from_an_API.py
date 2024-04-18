#!/usr/bin/python3
"""RESTful API for employee"""

import requests
import sys

def get_employee_tasks(user_id):
    """Returns information about an employee's tasks"""

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        employee_name = user_data.get('name')

        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        number_of_done_tasks = sum(1 for task in todos_data if task['completed'])
        total_number_of_tasks = len(todos_data)
        task_titles = [task['title'] for task in todos_data if task['completed']]

        print(f'Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):')

        for task_title in task_titles:
            print(f'\t{task_title}')

    except requests.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)