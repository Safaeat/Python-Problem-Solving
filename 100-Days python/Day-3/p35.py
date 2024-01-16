height = int(input("Enter your height(x cm): "))
bill = 0

if height >= 120:
  age = int(input("Enter your age: "))
  if age <18:
    bill = 5
    print("You have to pay 5$ for the ride.")
  elif age < 25:
    bill = 7
    print("You have to pay 7$ for the ride.")
  elif age >24:
    bill = 10
    print("You have to pay 10$ for the ride.")

  pic = input("Do you want to get picture?(2$ for click, reply y or n): ")
  if pic == "y":
    bill += 2
  print(f"Your total pay ammount is {bill}$")

else:
  print("You are not allowed.")

