import random

# if you have a list, you can randomly choose items from it...
colours = ["blue", "green", "red", "white", "yellow"]

list_2 = [
    ["sky", "blue"],
    ["grass", "green"],
    ["sun", "yellow"]
    ]

# choose random item from a list
random_q_a = random.choice(list_2)

question = random_q_a[0]
print(question)
answer = random_q_a[1]
print(answer)

print(random_q_a)

