import sys, os

amount = 0
while not amount:
    try:
        num = int(input("\nType the # of challenge: "))
        amount = int(input("Type the amount of problems in this challenge: "))
    except:
        pass

path_of_dir = f"ch{num}_challenge"
os.mkdir(path_of_dir) if not os.path.exists(path_of_dir) else None

for i in range(amount):
    open(f"{path_of_dir}/ch{num}_challenge{i+1}.py", "w")

print("Done.")
