#!/usr/bin/python3
"""
Fetches and displays information about an employee's TODO list progress
from a REST API.
"""

import sys
import requests


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # URLs for fetching employee info and TODOs
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    # Fetch data from API
    user = requests.get(user_url).json()
    todos = requests.get(todos_url).json()

    # Extract employee name and completed tasks
    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]

    # Print summary of completed tasks
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, len(done_tasks), len(todos)
        )
    )
    for task in done_tasks:
        print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    main()
