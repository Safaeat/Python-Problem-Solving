
for n in range(1, 101):
 if n%3 == 0:
  print(f"Fizz")
 elif n%5 == 0:
  print(f"Buzz")
 elif n%3 == 0 and n%5 == 0:
  print(f"FizzBuzz")
 else :
  print(f"{n}")