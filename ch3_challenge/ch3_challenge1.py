print("\nIt's so funny to look back to Python")
print("If only I can spend more time for Python..")
print("but eventhough Java is interesting too :]\n")

a = [1, 2, 3, 4]
# a=[print(f'{i} - {elem}' for i, elem in enumerate(a))]
# print("\n".join(f"{i+1} - {elem}" for i, elem in enumerate(a)))
# print('\n\n')


# squares = [x**2 for x in range(10) if x % 2 == 0]
# print(squares)  # Output: [0, 4, 16, 36, 64]

# squares2 = {x:x**2 for x in range(10) if x % 2 == 0}
# print(squares2)

# numbers = {x: "even" if x % 2 == 0 else "odd" for x in range(10)}
# print(numbers)

evens = lambda x: [i for i in x if i % 2 == 0]
evens = lambda x: [i if i % 2 == 0 else None for i in x]
print(evens([3, 4, 3, 2]))  # Output: [0, 2, 4, 6, 8]


squared = lambda x: list(map(lambda i: i**2, x))
print(squared([3, 4, 3, 2]))  # Output: [9, 16, 9, 4]

evens = lambda x: list(filter(lambda i: i % 2 == 0, x))
print(evens([3, 4, 3, 2]))  # Output: [4, 2]


evens = lambda x: [i for i in x if i % 2 == 0]
print(evens([3, 4, 3, 2]))  # Output: [4, 2]

# double_values = list(map({x: x * 2 for i in range(5)}))
# print(double_values)  # Output: [0, 2, 4, 6, 8]


def case_one():
    return "This is case one"


def case_two():
    return "This is case two"


cases = {1: case_one, 2: case_two}
print(cases.get(4, lambda: "Default case")())

list1 = [i + 1 for i in range(3)]
list2 = [i + 1 for i in range(3)]
matrix = [[i * j for j in list1] for i in list2]
print("\n".join(f"{elem}" for elem in matrix))


a, b, c = 1, 2, 3


def increase():
    global a, b, c
    c += 1
    a += 1
    b += 1


increase()
print(a, b, c)
