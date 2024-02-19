#!/usr/bin/python3
""" API -> CSV for one object """
import csv
import json
import sys
from urllib import request


def main():
    """executes ID_to_csv function"""
    try:
        employee_id = int(sys.argv[1])
        ID_to_csv(employee_id)
    except TypeError as e:
        pass


def ID_to_csv(employee_id):
    """ Uses REST API to return info about an employee\
         and pack it into an ID.csv file """

    # user url
    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # name of employee
    with request.urlopen(f"{url_user}") as user:
        name = json.loads(user.read()).get('username')

    # total tasks
    with request.urlopen(f"{url_user}/todos") as f:
        total_todo = json.loads(f.read())

    # create and write to file in CSV format
    file_path = f"{employee_id}.csv"

    with open(file_path, "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_ALL)
        for task in total_todo:
            csv_writer.writerow(
                [employee_id, name, task.get("completed"), task.get("title")]
                )


if __name__ == "__main__":
    main()
