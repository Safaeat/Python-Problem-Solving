import random

call = input("0 for Head and 1 for Tail: ")
print(f"The call is {call}.")
toss = random.randint(0, 1)
print(f"The random generated number is {toss}")

if toss == 0 and call == "0":
  print("You won the toss.")
elif toss == 1 and call == "1":
   print("You won the toss.")
else:
  print("You lose the toss.")