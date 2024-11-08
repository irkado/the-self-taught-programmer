import sys, os, csv, random

file_path = os.path.join(os.getcwd(), "additional", "employees.csv")
fieldnames = ["Name", "Age", "Department", "Salary"]

info_dict = {
    "Name": ["Alice", "Bob", "Carol", "David"],
    "Age": [20, 80],
    "Department": ["HR", "Engineering", "Marketing", "Sales"],
    "Salary": [3000, 100000],
}


def gener_employees(num):
    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, "w") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()

        new_dict = {}
        for i in range(num):
            new_dict = {
                key: (
                    info_dict[key][random.randint(0, len(info_dict[key]) - 1)]
                    if key == "Name" or key == "Department"
                    else random.randint(info_dict[key][0], info_dict[key][1] + 1)
                )
                for key in fieldnames
            }

            w.writerow(new_dict)

    print("New csv file was generated\n")


if __name__ == "__main__":
    gener_employees(100)
