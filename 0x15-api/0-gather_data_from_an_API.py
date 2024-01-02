#!/usr/bin/python3
"""
Return information for a given employee about his/her TODO list progress
"""
import requests
import sys

def get_user_data(employee_id):
    url_for_users = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    response = requests.get(url_for_users)

    if response.status_code != 200:
        print("Error: Unable to fetch user data")
        sys.exit(1)

    return response.json()

def get_todo_data(employee_id):
    url_for_todos = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url_for_todos)

    if response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        sys.exit(1)

    todos = response.json()
    return [todo for todo in todos if todo.get('userId') == employee_id]

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data = get_user_data(employee_id)
    todo_data = get_todo_data(employee_id)

    done_tasks = sum(1 for todo in todo_data if todo.get('completed'))
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):".format(user_data.get('name'), done_tasks, total_tasks))

    for todo in todo_data:
        if todo.get('completed'):
            print("\t{}".format(todo.get('title')))
