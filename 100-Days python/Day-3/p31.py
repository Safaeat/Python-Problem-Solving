height = int(input("Enter your height(x cm): "))

if height >= 120:
  age = int(input("Enter your age: "))
  if age <18:
    print("You have to pay 7$.")
  else:
    print("You have to pay 18$.")
else:
  print("You are not allowed.")