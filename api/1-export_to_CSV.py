#!/usr/bin/python3
'''Export data in the CSV format'''

import csv
import requests
from sys import argv


def csv_format():

    u_id = argv[1]
    api_url = f"https://jsonplaceholder.typicode.com/users/{u_id}"
    api_url2 = f"https://jsonplaceholder.typicode.com/todos?userId={u_id}"
    
    user_response = requests.get(api_url)
    user_data = user_response.json()
    
    if isinstance(user_data, list):
        user_data = user_data[0]
    
    EMPLOYEE_NAME = user_data.get('name')
    
    todos_response = requests.get(api_url2)
    todos_data = todos_response.json()
    
    f_name = f"{u_id}.csv"
    
    with open(f_name, 'w', newline='', encoding='utf-8') as f:
        csvwriter = csv.writer(f)
        
        csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for info in todos_data:
            TASK_COMPLETED_STATUS = info.get("completed")
            TASK_TITLE = info.get("title")
            
            csvwriter.writerow([u_id, EMPLOYEE_NAME, TASK_COMPLETED_STATUS, TASK_TITLE])

if __name__ == '__main__':
    if len(argv) != 2:
        print(f"UsageError: python3 {__file__} employee_id(int)")
    else:
        csv_format()