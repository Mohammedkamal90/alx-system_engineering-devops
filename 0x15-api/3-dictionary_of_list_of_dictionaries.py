#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
gathers data from API
"""
import json
import requests


API = "https://jsonplaceholder.typicode.com"


def get_user_data():
    users_res = requests.get('{}/users'.format(API)).json()

    if 'message' in users_res and 'Not Found' in users_res['message']:
        print("Error: Unable to fetch user data")
        return []

    return users_res


def get_todo_data():
    todos_res = requests.get('{}/todos'.format(API)).json()

    if 'message' in todos_res and 'Not Found' in todos_res['message']:
        print("Error: Unable to fetch TODO list data")
        return []

    return todos_res


def export_to_json(users_data):
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)


if __name__ == '__main__':
    users_data = {}
    users_res = get_user_data()
    todos_res = get_todo_data()

    for user in users_res:
        user_id = str(user.get('id'))
        user_name = user.get('username')
        todos = [todo for todo in todos_res if todo.get('userId') == user_id]

        user_data = [
            {
                'username': user_name,
                'task': todo.get('title'),
                'completed': todo.get('completed')
            } for todo in todos
        ]

        users_data[user_id] = user_data

    export_to_json(users_data)
