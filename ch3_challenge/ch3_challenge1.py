print("\nIt's so funny to look back to Python")
print("If only I can spend more time for Python..")
print("but eventhough Java is interesting too :]\n")

# Additional code :] or HOW TO PRINT ARRAY
a = [1, 2, 3, 4]

[print(f"{i+1} - {elem}, ", end="") for i, elem in enumerate(a)]
print()

print(", ".join(f"{elem}" if elem % 2 != 0 else "x" for elem in a))

print()
print("\n".join(f"{i+1} - {elem}" for i, elem in enumerate(a)))
