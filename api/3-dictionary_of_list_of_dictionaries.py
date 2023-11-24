"""
Python script to export data in the JSON format
"""

import requests
import json

url = 'https://jsonplaceholder.typicode.com'

users_res = requests.get(f'{url}/users')
users = users_res.json()

todos_res = requests.get(f'{url}/todos')
todos = todos_res.json()

tasks_by_user = {}

for user in users:
    user_id = str(user['id'])
    username = user['username']
    tasks_by_user[user_id] = []

    for todo in todos:
        if str(todo['userId']) == user_id:
            task_data = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': username
            }
            tasks_by_user[user_id].append(task_data)

with open('todo_all_employees.json', 'w') as file:
    json.dump(tasks_by_user, file, indent=2)
