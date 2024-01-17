import random
name = input("Input tha names(Ex: rana, mina, tina): ")

list = name.split(", ")
member = len(list)
print(f"Total number of member is {member}.")
print(list)
# index = random.randint(0, member-1)
# print(f"{list[index]} is going to buy meal today!")

index = random.choice(list)
print(f"{index} is going to buy meal today!")
