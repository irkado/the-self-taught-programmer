a = int(input("type some int value: "))
x = lambda a: (
    "the smallest" if a < 10 else "in the middle" if a > 10 and a <= 25 else "large one"
)

print(x(a), end="\n\n")
