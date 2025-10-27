#!/usr/bin/python3
"""
Fetch and display an employee’s TODO list progress from the JSONPlaceholder API.

This script takes an employee ID as a command-line argument, retrieves the
employee’s name and their list of tasks, and displays the number of completed
tasks out of the total. It then lists the titles of the completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Example:
    python3 0-gather_data_from_an_API.py 2
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetch and display an employee’s task completion status.

    Args:
        employee_id (str): The ID of the employee whose tasks will be fetched.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_response.raise_for_status()
    user_data = user_response.json()

    employee_name = user_data.get("name")

    # Fetch tasks
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_response.raise_for_status()
    todos_data = todos_response.json()

    # Filter completed tasks
    done_tasks = [task for task in todos_data if task.get("completed")]

    # Display the results in the required format
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{len(todos_data)}):")
    for task in done_tasks:
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        get_employee_todo_progress(sys.argv[1])
    except requests.exceptions.RequestException:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)
