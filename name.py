import random

first_names = ["Amy", "Kate", "Emma"]
last_names = ["Johnson", "Smith", "Williams"]

group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(1))

print(group)
