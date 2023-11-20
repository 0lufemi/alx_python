"""
Python script that returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == '__main__':
    """
    Employee details
    """
    employee_id = sys.argv[1]
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_res = requests.get(employee_url)
    employee_json = employee_res.json()

    """
    Employee todo list
    """
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_res = requests.get(todo_url)
    todo_json = todo_res.json()

    total_tasks = len(todo_json)

    completed_tasks = 0
    for task in todo_json:
        if (task['completed']):
            completed_tasks += 1

    # print(todo_json)

    #Display Output
    print(f"Employee {employee_json['name']} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_json:
        if (task['completed']):
            print(f"\t {task['title']}")
