#!/usr/bin/python3
"""
Export data about tasks owned by an employee in JSON format
"""
import json
import requests
import sys
if __name__ == "__main__":

    DONE_TASKS = 0
    ALL_TASKS = 0
    csvList = []

    URL_FOR_USERS = 'https://jsonplaceholder.typicode.com/users/{0}'.\
        format(sys.argv[1])
    URL_FOR_TODOS = 'https://jsonplaceholder.typicode.com/todos'
    r_for_users = requests.get(URL_FOR_USERS)
    r_for_todos = requests.get(URL_FOR_TODOS)

    name = r_for_users.json().get('name')
    user_name = r_for_users.json().get('username')
    todos = r_for_todos.json()
    with open(sys.argv[1] + '.json', 'w+') as f:
        json.dump({sys.argv[1]: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user_name} for todo in todos]}, f)
