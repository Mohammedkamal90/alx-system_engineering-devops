#!/usr/bin/python3
"""
Export data about tasks owned by an employee in CSV format
"""
import requests
import sys
import csv

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

def export_to_csv(user_data, todo_data):
    user_id = user_data.get('id')
    username = user_data.get('username')
    filename = '{}.csv'.format(user_id)

    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todo_data:
            task_completed_status = str(todo.get('completed'))
            task_title = todo.get('title')
            csv_writer.writerow([user_id, username, task_completed_status, task_title])

    print("Data exported to {}".format(filename))

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])

    user_data = get_user_data(employee_id)
    todo_data = get_todo_data(employee_id)

    export_to_csv(user_data, todo_data)
