import random

list_2= [
    ["Italy", "Rome"],
    ["Spain", "Madrid"],
    ["United States", "Washington DC"],
    ["United Kingdom", "London"],
    ["New Zealand", "Wellington"],
    ["Australia", "Canberra"],
    ["South Africa", "Pretoria"],
    ["Russia", "Moscow"],
    ["Japan", "Tokyo"]
    ]

random_q_a = random.choice(list_2)
question = random_q_a[0]
print(question)
answer = random_q_a[1]
print(answer)

print(random_q_a)