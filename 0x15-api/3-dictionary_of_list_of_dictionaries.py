#!/usr/bin/python3
""" API -> JSON for all objects """
import json
import sys
from urllib import request


def main():
    """executes all_to_json function"""

    all_to_json()


def all_to_json():
    """ Uses REST API to return info about an employee\
         and pack it into an ID.json file """

    task_dict = {}
    # user url
    url_user = f"https://jsonplaceholder.typicode.com/users"

    # all users
    with request.urlopen(f"{url_user}") as all_users:
        users = json.loads(all_users.read())
    for guy in users:
        # employee id
        employee_id = guy.get('id')

        # name of employee
        name = guy.get('username')

        # total tasks of each guy
        with request.urlopen(f"{url_user}/{employee_id}/todos") as f:
            total_todo = json.loads(f.read())
            task_dict[employee_id] = []
            for task in total_todo:
                task_dict[employee_id].append({
                    'task': task.get("title"),
                    "completed": task.get("completed"),
                    "username": name
                })

    # decode content
    task_json = json.JSONEncoder().encode(task_dict)

    # create and write to file in JSON format
    file_path = "todo_all_employees.json"

    with open(file_path, "w") as json_file:
        json_file.write(task_json)


if __name__ == "__main__":
    main()
