#!/usr/bin/python3
"""
Using https://jsonplaceholder.typicode.com
returns info about employee TODO progress
Implemented using recursion
"""
import re
import requests
import sys

API = "https://jsonplaceholder.typicode.com"
"""REST API url"""


def get_user_data(employee_id):
    user_res = requests.get('{}/users/{}'.format(API, employee_id))
    user_data = user_res.json()

    if user_res.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)

    return user_data


def get_todo_data():
    todos_res = requests.get('{}/todos'.format(API))
    todos_data = todos_res.json()

    if todos_res.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)

    return todos_data


def print_todo_progress(user_name, todos_done, total_todos):
    print(
        'Employee {} is done with tasks({}/{}):'.format(
            user_name, len(todos_done), total_todos
        )
    )
    for todo_done in todos_done:
        print('\t {}'.format(todo_done.get('title')))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            employee_id = int(sys.argv[1])

            user_data = get_user_data(employee_id)
            user_name = user_data.get('name')

            todos_data = get_todo_data()
            todos = list(filter(lambda x: x.get('userId') == employee_id, todos_data))
            todos_done = list(filter(lambda x: x.get('completed'), todos))

            print_todo_progress(user_name, todos_done, len(todos))
