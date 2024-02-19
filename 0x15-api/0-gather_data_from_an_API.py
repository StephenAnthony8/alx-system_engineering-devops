#!/usr/bin/python3
""" API intro practise module """
import json
import sys
from urllib import request, error


def main():
    """executes request_get function"""
    try:
        employee_id = int(sys.argv[1])
        request_get(employee_id)
    except TypeError as e:
        pass


def request_get(employee_id):
    """ Uses REST API to return info about an employees TODO list """

    # user url
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # name of employee
    with request.urlopen(f"{url_user}") as user:
        name = json.loads(user.read()).get('name')

    # number of total tasks
    with request.urlopen(f"{url_user}/todos") as f:
        total_todo = len(json.loads(f.read()))

    # completed tasks
    with request.urlopen(f"{url_user}/todos?completed=true") as f:
        true_complete = json.loads(f.read())

    complete_status = f"{len(true_complete)}/{total_todo}"

    # output
    print(f"Employee {name} is done with tasks({complete_status}):")
    for task in true_complete:
        print(f"     {task.get('title')}")


if __name__ == "__main__":
    main()
