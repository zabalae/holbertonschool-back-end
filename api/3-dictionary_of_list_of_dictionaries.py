#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests


if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"

    users = requests.get(url + "users").json()

    datas = {}
    for user in users:
        user_id = user["id"]
        user_url = url + f"todos?userId={user_id}"
        todo_list = requests.get(user_url).json()

        datas[user_id] = [
            {"task": todo.get("title"),
             "completed": todo.get("completed"),
             "username": user.get("username"),}
            for todo in todo_list]

    with open('todo_all_employees.json', 'w') as f:
        json.dump(datas, f)
