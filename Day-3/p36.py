print("Welcome to Python Pizza Deliveries!")
bill =0

size = input("What size pizza do you want? s, m or l: ")
if size == "s":
  bill = 15
  print("Small Pizza: 15$")
elif size == "m":
  bill = 20
  print("Medium Pizza: 20$")
elif size == "l":
  bill = 25
  print("Large Pizza: 25$")
else:
  print("Wrong input. inter s for small, m for large or l for large.")

add_pepperoni = input("Do you want pepperoni? y or n: ")
if  add_pepperoni == "y":
  pepperoni = input("for small, type s and for medium or large, type l: ")
  if pepperoni == "s":
   bill += 2
   print("Pepperoni for small pizza: 2$")
  elif pepperoni == "l":
   bill +=3
   print("pepperoni for medium or large: 3$")
  else:
   print("Wrong input.")
else:
  print("No pepperoni.")

cheese = input("Extra cheese? y or n: ")
if cheese == "y":
  bill += 1
  print("Extra cheese for any pizza: 1$")
else:
  ("No cheese.")

print(f"You have to pay totoal {bill}$,")
