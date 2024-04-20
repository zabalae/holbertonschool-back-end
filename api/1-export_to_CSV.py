#!/usr/bin/python3
"""RESTful API for employee"""

import csv
import requests
import sys


def get_employee_tasks(employee_id):

    employee_name = ""
    number_of_done_tasks = 0
    total_number_of_tasks = 0
    task_titles = []

    url_users = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_T = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(url_users)
    user_data = user_response.json()

    if isinstance(user_data, list):
        user_data = user_data[0]

    employee_name = user_data.get('name')

    todos_response = requests.get(url_T)
    todos_data = todos_response.json()

    for task in todos_data:
        total_number_of_tasks += 1
        if task['completed']:
            number_of_done_tasks += 1
            task_titles.append(task['title'])

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["USER_ID","USERNAME", "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"])
        csvwriter.writerows(todos_data)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_tasks(employee_id)
