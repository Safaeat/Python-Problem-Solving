#Write a Python program to find an odd number between 1 to 200.


start, end = 1, 100
for num in range(start, end + 1):
 
 if num % 2 != 0:
   print(num, end = " ")