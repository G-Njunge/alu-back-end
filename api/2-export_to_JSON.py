#!/usr/bin/python3
"""
Exports an employee's TODO list to a CSV file.
"""

import json
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

    # writing the api response in a json format
    filename = f"{employee_id}.json"

    json_data = {
        employee_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username  
            }
            for task in todos
        ]  
    }
    with open(filename, "w") as json_file:
        json.dump(json_data, json_file)