#!/usr/bin/python3
"""RESTFul API for employee"""
import requests
import sys


if __name__ == "__main__":

    """Returns information about employees"""
    id = int(sys.argv[1])
    number_of_done_tasks = 0
    total_number_of_tasks = 0
    task_title = []

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id).json()
    employee_name = user_url.get('name')
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + id + "/todos").json()

    for task in todos:
        if task.get('userId') == id:
            if task.get('completed') is True:
                task_title.append(task['title'])
                number_of_done_tasks += 1
            total_number_of_tasks += 1

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
          number_of_done_tasks, total_number_of_tasks))

    for j in task_title:
        print("\t {}".format(j))