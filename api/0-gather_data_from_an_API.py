#!/usr/bin/python3
"""
A script that uses a REST API to return information
about an employee’s TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    # Ensure an employee ID is provided
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user and todo data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Display results in the required format (PEP 8 compliant)
    print(
        f"Employee {employee_name} is done with tasks("
        f"{len(done_tasks)}/{total_tasks}):"
    )
    for task in done_tasks:
        print(f"\t {task.get('title')}")