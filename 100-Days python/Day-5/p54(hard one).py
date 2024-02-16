#Password Generator Project(easy one)
import random
letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

letters= int(input("How many letters would you like in your password?\n"))
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))


password_list = []
for char in range (1, letters + 1):
  password_list.append(random.choice(letter))
for char in range(1, symbols + 1):
  password_list.append(random.choice(symbol))
for char in range(1, numbers + 1):
  password_list.append(random.choice(number))
print(password_list)
random.shuffle(password_list)
print(password_list)

final =""
for ch in password_list:
 final += ch
print(f"your password is:",final)
