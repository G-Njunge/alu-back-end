#!/usr/bin/python3
"""
Exports an employee's TODO list to a CSV file.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    # Ensure an employee ID is provided
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user and todo data
    user = requests.get(f"{base_url}/users/{employee_id}").json()
    todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()

    username = user.get("username")

    # CSV file name: USER_ID.csv
    filename = f"{employee_id}.csv"

    # Write CSV file
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])