import sys, os, csv, random
from gener_of_emplo import file_path, fieldnames
from rich import print
from rich.traceback import install

"""
Task 1: CSV Data Processing and File Management

Goal: Enhance skills in reading and writing CSV files, working with dictionaries, and managing files and directories.

Write a Python program that:
° Reads a CSV file named employees.csv with columns: "Name", "Age", "Department", "Salary".
° For each row, create a dictionary representing the employee's data.
Calculate the average salary of employees and print it.
Writes employees into separate CSV files based on their department (e.g., HR.csv, Engineering.csv) in a directory named departments.
Use os to:
Check if the departments directory exists, and create it if it doesn’t.
Clean up by removing any existing CSV files in the departments directory before saving new ones.
"""

install()

while 1:
    user_input = input("\nType a prompt: ").lower().strip()

    if user_input == "read":
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                r = csv.DictReader(f)

                names, emplo_dict = {}, {}
                for row in r:

                    names[row["Name"]] = (
                        names[row["Name"]] + 1 if row["Name"] in names.keys() else 1
                    )

                    emplo_dict[
                        f'{row["Name"]} {names[row["Name"]] if names[row["Name"]]>1 else""}'.strip()
                    ] = {key: row[key] for key in fieldnames if key != "Name"}

                print(emplo_dict)
        else:
            print("That file does not exist")

    elif user_input == "x":
        sys.exit()

    else:
        print("Try again with another prompt")
