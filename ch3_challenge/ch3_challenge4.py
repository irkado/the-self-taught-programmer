a = int(input("First var value: "))
b = int(input("Second var value: "))

print(float(a / b))
print(f"{a%b} - the remainder from division :)")

# Additional code
print("\n\n" + " ".join("Matrix"))

list1, list2 = [i + 1 for i in range(3)], [i + 1 for i in range(4,7)]

matrix = [[i * j for j in list1] for i in list2]
print("\n".join(f"{elem}" for elem in matrix))
