#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""
import json
import requests
import sys


def get_user_data(employee_id):
    url_for_users = 'https://jsonplaceholder.typicode.com/users/{}'
            .format(employee_id)
    response = requests.get(url_for_users)

    if response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)

    return response.json()


def get_todo_data():
    url_for_todos = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url_for_todos)

    if response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)

    return response.json()


def export_to_json(user_id, username, todo_data):
    filename = '{}.json'.format(user_id)

    json_data = {str(user_id): []}

    for todo in todo_data:
        task_title = todo.get('title')
        task_completed_status = todo.get('completed')
        json_data[str(user_id)].append({
            "task": task_title,
            "completed": task_completed_status,
            "username": username})

    with open(filename, 'w+') as json_file:
        json.dump(json_data, json_file)

    print("Data exported to {}".format(filename))


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data = get_user_data(employee_id)
    todo_data = get_todo_data()

    export_to_json(employee_id, user_data.get('username'), todo_data)
