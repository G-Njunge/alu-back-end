#!/usr/bin/python3

import json
import requests
import sys

base_url = "https://jsonplaceholder.typicode.com"
def employee_task(employee_id):
	try:
		employee_raw_data = requests.get(f"{base_url}/users/{employee_id}")
		employee_parsed = employee_raw_data.json()
		employee_name = employee_parsed.get("name")
		tasks = requests.get(f"{base_url}/todos?userId={employee_id}")
	
		completed_tasks = []
		for i in tasks:
			if (i.get("completed")):
				completed_tasks.append(i)

		print(f" Employee {employee_name} is done with tasks ({len(completed_tasks}/{len(tasks)}):")
		for completed_task in completed_tasks:
			print(f"\t {completed_task.get('title')}")
	except request.exception.RequestException as e:
		print("unable to connect")
		sys.exit(1)
	
if __name__ == "__main__":
	employee_id = int(sys.argv[1])
	employee_task(employee_id)

	
		
