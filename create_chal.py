import sys

num = int(input("Type the num of challenges: "))
amount = int(input("Type the amount of files: "))

for i in range(amount):
    with open(f"ch{num}_challenge/ch{num}_challenge{i+1}.py",'w') as my_file:
        pass
