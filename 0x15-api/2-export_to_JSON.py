#!/usr/bin/python3
""" API -> JSON for one object """
import json
import sys
from urllib import request


def main():
    """executes ID_to_json function"""
    try:
        employee_id = int(sys.argv[1])
        ID_to_json(employee_id)
    except TypeError as e:
        pass


def ID_to_json(employee_id):
    """ Uses REST API to return info about an employee\
         and pack it into an ID.json file """

    # user url
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # name of employee
    with request.urlopen(f"{url_user}") as user:
        name = json.loads(user.read()).get('username')

    # total tasks
    with request.urlopen(f"{url_user}/todos") as f:
        total_todo = json.loads(f.read())

        task_dict = {employee_id: []}
        for task in total_todo:
            task_dict[employee_id].append({
                'task': task.get("title"),
                "completed": task.get("completed"),
                "username": name
            })

        task_json = json.dumps(task_dict)

    # create and write to file in JSON format
    file_path = f"{employee_id}.json"

    with open(file_path, "w") as json_file:
        json.dump(task_json, json_file, ensure_ascii=True)


if __name__ == "__main__":
    main()
