#!/usr/bin/python3
"""RESTful API for employee"""
import csv
import requests
import sys


def get_employee_tasks(employee_id):

    employee_name = ""
    task_data = []

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_T = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(user_url)
    user_data = user_response.json()

    if isinstance(user_data, list):
        user_data = user_data[0]

    employee_name = user_data.get('name')

    tasks_response = requests.get(url_T)
    tasks_data = tasks_response.json()

    for task in tasks_data:
        task_data.append([
            employee_id,
            employee_name,
            str(task['completed']),
            task['title']
        ])

    filename = f"{employee_id}.csv"
    with open(filename, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for i in url_T.json():
            writer.writerow([employee_id, employee_name,
                             i.get('completed'), i.get('title')])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_tasks(employee_id)
