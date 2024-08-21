#!/usr/bin/python3
"""docs are docs"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    empId = sys.argv[1]
    res1 = requests.get(url+"users"+f"?id={empId}")
    empName = res1.json()[0]['username']

    res2 = requests.get(url+"todos"+f"?userId={empId}")
    res2 = res2.json()
    with open('USER_ID.csv', 'w') as f:
        for task in res2:
            line = f"\"{empId}\",\"{empName}\","
            line += f"\"{task['completed']}\",\"{task['title']}\"\n"
            f.write(line)
