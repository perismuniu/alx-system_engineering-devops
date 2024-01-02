#!/usr/bin/python3
"""
Script to gather data from an API for a given employee ID and export to CSV.
"""

import requests
import csv
from sys import argv


def export_to_csv(employee_id, user_data, todo_data):
    """
    Export data to CSV file.
    """
    filename = "{}.csv".format(employee_id)

    with open(filename, mode='w', newline='') as csvfile:
        fieldnames = ['USER_ID', 'USERNAME',
                      'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': user_data.get('name'),
                'TASK_COMPLETED_STATUS': str(task.get('completed')),
                'TASK_TITLE': task.get('title')
            })


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: {} <employee_id>".format(argv[0]))
    else:
        employee_id = argv[1]
        base_url = "https://jsonplaceholder.typicode.com"

        # Fetch user information
        user_response = requests.get("{}/users/{}"
                                     .format(base_url, employee_id))
        user_data = user_response.json()

        # Fetch TODO list for the user
        todo_response = requests.get("{}/todos?userId={}"
                                     .format(base_url, employee_id))
        todo_data = todo_response.json()

        # Export to CSV
        export_to_csv(employee_id, user_data, todo_data)
