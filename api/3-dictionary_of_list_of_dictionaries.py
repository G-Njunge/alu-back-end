#!/usr/bin/python3
"""
Exports an employee's TODO list to a CSV file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    #putting the base url in a variable for cleaber code
    base_url = "https://jsonplaceholder.typicode.com"

    #creating an empty dict where I can have all my tasks
    total_employee_data = {}

    #loopin through the individual ids
    employees_data = requests.get(f"{base_url}/users").json()
    for employee_data in employees_data:
        employee_id =employee_data.get("id")
        user = requests.get(f"{base_url}/users/{employee_id}").json()
        todos = requests.get(f"{base_url}/todos?userId={employee_id}").json()
        username = user.get("username")

         #json data format
        json_data = {
            employee_id: [
                {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
                }
                for task in todos
            ]
        }
        total_employee_data.update(json_data)

    filename = "todo_all_employees.json"
    with open(filename, "w") as json_file:
        json.dump(total_employee_data, json_file)
       

    
        

       
       


