height = int(input("Enter your height(x cm): "))

if height >= 120:
  age = int(input("Enter your age: "))
  if age <12:
    print("You have to pay 7$.")
  elif age <= 17:
    print("You have to pay 18$.")
  else:
    print("You have to pay 50$.")
else:
  print("You are not allowed.")