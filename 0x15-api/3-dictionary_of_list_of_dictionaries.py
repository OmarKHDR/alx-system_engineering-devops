#!/usr/bin/python3
"""docs are docs"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    res1 = requests.get(url+"users/").json()

    users_obj = {}
    for user in res1:
        user_arr = []
        print(user_arr)
        res2 = requests.get(url+"todos/"+f'?{user["id"]}').json()
        for task in res2:
            task['username'] = user['name']
            task['task'] = task['title']
            del task['id'], task['userId'], task['title']
            user_arr.append(task)
        users_obj[str(user["id"])] = user_arr[:]
        del user_arr

    json_obj = json.dumps(users_obj)
    with open("todo_all_employees.json", 'w') as f:
        f.write(json_obj)
