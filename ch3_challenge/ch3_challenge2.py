a = 0
while not a:
    try:
        a = int(input("\nType some value: "))
    except:
        print("Try again :0")


print("oh yeah" if a >= 10 else "too small", end="\n\n")

# Additional code about ternary operators && dicts
squares = [x**2 for x in range(10) if x % 2 == 0]
print(squares)  # Output: [0, 4, 16, 36, 64]

squares2 = {x: x**2 for x in range(10) if x % 2 == 0}
print(squares2)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
