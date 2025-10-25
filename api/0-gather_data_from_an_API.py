#!/usr/bin/python3
"""
This script retrieves and displays an employee's completed tasks from a fake REST API.

The program uses the JSONPlaceholder API to fetch:
- Employee details (name)
- Tasks assigned to the employee

It then prints:
- The employee’s name
- How many tasks they have completed out of the total
- The titles of all completed tasks

Usage:
    python3 script_name.py <employee_id>

Example:
    python3 employee_tasks.py 2
"""

import sys
import requests

# Base URL of the fake REST API
BASE_URL = "https://jsonplaceholder.typicode.com"

def employee_task(employee_id):
    """
    Fetch and display an employee's completed tasks.

    Args:
        employee_id (int): The ID of the employee.

    Raises:
        SystemExit: If there is a connection or request error.
    """
    try:
        # Fetch employee details
        employee_response = requests.get(f"{BASE_URL}/users/{employee_id}")
        employee_response.raise_for_status()  # Raises an error for bad responses (e.g. 404, 500)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetch tasks for the employee
        tasks_response = requests.get(f"{BASE_URL}/todos?userId={employee_id}")
        tasks_response.raise_for_status()
        tasks = tasks_response.json()

        # Filter completed tasks
        completed_tasks = [task for task in tasks if task.get("completed")]

        # Print summary
        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{len(tasks)}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException:
        print("Unable to connect to the API.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)
    try:
        employee_id = int(sys.argv[1])
        employee_task(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
		
