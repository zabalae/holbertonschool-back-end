#!/usr/bin/python3
'''Export data in the CSV format'''

import csv
import requests
import sys


def csv_format():

    user_response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    username = user_data.get('username')

    todos_response = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todos_data = todos_response.json()

    with open(f"{employee_id}.csv", 'w', newline='', 
              encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        csvwriter.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        )

        for task in todos_data:
            task_completed = task.get("completed")
            task_title = task.get("title")
            csvwriter.writerow(
                [employee_id, username, task_completed, task_title]
            )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
        sys.exit(1)

    employee_id = sys.argv[1]
    csv_format(employee_id)
