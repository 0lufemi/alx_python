"""
Python script to export data in the CSV format.
"""

import requests
import sys
import csv

if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_res = requests.get(employee_url)
    employee_json = employee_res.json()

    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_res = requests.get(todo_url)
    todo_json = todo_res.json()

    with open(f"{employee_id}.csv", "w") as csvfile:
        f = csv.writer(csvfile)
        f.writerow(["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"])
        for task in todo_json:
            f.writerow([employee_id, employee_json['username'], task['completed'], task['title']])
