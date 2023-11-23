import json
import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_res = requests.get(employee_url)
    employee_json = employee_res.json()

    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    todo_res = requests.get(todo_url)
    todo_json = todo_res.json()

    result = {employee_id: []}

    for task in todo_json:
        task_data = {
            'task': task['title'],
            'completed': task['completed'],
            'username': employee_json['username']
        }
        result[employee_id].append(task_data)

    with open(f"{employee_id}.json", "w") as file:
        json.dump(result, file)
