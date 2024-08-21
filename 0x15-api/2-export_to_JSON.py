#!/usr/bin/python3
"""docs are docs"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empId = sys.argv[1]
    res1 = requests.get(url+"users"+f"?id={empId}")
    empName = res1.json()[0]['username']

    res2 = requests.get(url+"todos"+f"?userId={empId}")
    res2 = res2.json()
    user_arr = []
    for task in res2:
        task['username'] = empName
        task['task'] = task['title']
        del task['id'], task['userId'], task['title']
        user_arr.append(task)

    obj = {f'{empId}': user_arr}
    json_obj = json.dumps(obj)
    with open(f"{empId}.json", 'w') as f:
        f.write(json_obj)
