import random

sides = ["salad", "chicken noodle soup", "garlic bread"]
main_courses = ["chicken", "salmon", "steak"]
dessert = ["chocolate cake", "strawberry ice cream", "fruit"]

group=" ".join(random.choice(sides)+" "+random.choice(main_courses)+" "+random.choice(dessert)for _ in range(1))

print (group)
