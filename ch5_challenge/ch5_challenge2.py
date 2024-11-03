dict_with_tup = {"pi": (3.14, 34), "k": (44444), "g": (9.81, 34)}

print(
    "\n".join(
        f"{i+1} - {x} : {dict_with_tup[x]}" for i, x in enumerate(dict_with_tup.keys())
    )
)
