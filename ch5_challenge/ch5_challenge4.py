dict_of_que = {
    "weight": "What's your weight",
    "hobby": "What’s a hobby you picked up recently",
    "accomplishment": "Is there an accomplishment you’re really proud of",
}
dict_of_ans = {}

for key in dict_of_que.keys():
    print(dict_of_que[key], end="")
    user_input = input(": ")
    dict_of_ans[key] = user_input

print("\nquestion ---> your answer :)\n")
print("\n".join(f"{dict_of_que[key]} ---> {dict_of_ans[key]}" for key in dict_of_ans))
