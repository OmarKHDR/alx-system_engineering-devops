#!/usr/bin/python3
""" docs IS imp """

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    params = {"userId": employee_id}
    res = requests.get("https://jsonplaceholder.typicode.com/todos/", params=params)
    res2 = requests.get("https://jsonplaceholder.typicode.com/users/", params={'id': employee_id})

    done_tasks = []
    completed = 0
    total = 0
    res = res.json()
    res2 = res2.json()
    name = res2[0]['name']
    for task in res:
        total += 1
        if task['completed']:
            done_tasks.append(task['title'])
            completed += 1
    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for task in done_tasks:    
        print(f"\t{task}")
