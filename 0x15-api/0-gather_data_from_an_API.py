#!/usr/bin/python3
"""
Script to gather data from an API for a given employee ID.
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = int(argv[1])
        base_url = "https://jsonplaceholder.typicode.com"

        # Fetch user information
        user_response = requests.get("{}/users/{}"
                                     .format(base_url, employee_id))
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch TODO list for the user
        todo_response = requests.get("{}/todos?userId={}"
                                     .format(base_url, employee_id))
        todo_data = todo_response.json()

        # Calculate completed tasks and total tasks
        completed_tasks = [task for task in todo_data if task.get('completed')]
        total_tasks = len(todo_data)
        num_completed_tasks = len(completed_tasks)

        # Display the information
        print("Employee {} is done with tasks({}/{}):"
              .format(employee_name, num_completed_tasks, total_tasks))
        for task in completed_tasks:
            print("\t {}".format(task.get('title')))
