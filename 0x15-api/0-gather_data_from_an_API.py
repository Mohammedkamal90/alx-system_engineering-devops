#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    employee_id = int(argv[1])

    # API endpoints
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)

    # Fetching user data
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    # Check if the requests were successful
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        exit(1)

    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODO list data")
        exit(1)

    # Parse user data
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Parse TODO list data
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get('completed')]

    # Displaying employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))

