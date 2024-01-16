print("Welcome to True Love calculator.")
true=0
love=0

n1 = input("Input the boy name: ").lower()
n2 = input("Input the girl name: ").lower()

true += n1.count('t')
true += n1.count('r')
true += n1.count('u')
true += n1.count('e')

love += n2.count('l')
love += n2.count('o')
love += n2.count('v')
love += n2.count('e')

per = int(str(true) + str(love))

if per < 10 or per > 90:
  print(f"Your score is {per}, you go together like coke and mentos.")
elif per >= 40 and per <= 50:
  print(f"Your score is {per}, you are alright together.")
else:
  print(f"Your score is {per}.")