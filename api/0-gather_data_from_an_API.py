#!/usr/bin/python3
"""
Fetch and display employee task completion data from JSONPlaceholder API.

This script retrieves information about a specific employee and their tasks,
then prints how many tasks they've completed along with the titles of those
tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys

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
        employee_response = requests.get(
            f"{BASE_URL}/users/{employee_id}"
        )
        employee_response.raise_for_status()
        employee_data = employee_response.json()
        EMPLOYEE_NAME = employee_data.get("name")

        tasks_response = requests.get(
            f"{BASE_URL}/todos?userId={employee_id}"
        )
        tasks_response.raise_for_status()
        tasks = tasks_response.json()

        completed_tasks = [t for t in tasks if t.get("completed")]

        print(f"Employee {EMPLOYEE_NAME} is done with tasks({len(completed_tasks)}/{len(tasks)}):")
        for task in completed_tasks:
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException:
        print("Unable to connect to the API.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        employee_task(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)
