a = int(input("type some int value: "))
x = lambda a: (
    "the smallest" if a < 10 else "in the middle" if a > 10 and a <= 25 else "large one"
)

print(x(a), end="\n\n")

# Additional code: ALL about LAMBDA :]
evens = lambda x: [i for i in x if i % 2 == 0]
print(evens([3, 4, 3, 2]))  # [4, 2]
evens = lambda x: [i if i % 2 == 0 else "" for i in x]
print(evens([3, 4, 3, 2]))  # ['', 4, '', 2]

print()

double_values = list(map(lambda x: x * 2, range(5)))
print("doubles ", double_values)


map_1 = lambda x: list(map(lambda i: i**2, x))
print("map ", map_1([3, 4, 3, 2]))

filter_1 = lambda x: list(filter(lambda i: i % 2 == 0, x))
print("filter ", filter_1([3, 4, 3, 2]))


def case_one():
    return "\nThis is case one"
def case_two():
    return "\nThis is case two"
cases = {1: case_one, 2: case_two}
print(cases.get(4, lambda: "\nDefault case")())
