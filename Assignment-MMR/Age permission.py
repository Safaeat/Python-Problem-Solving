'''
Write a Python program that will take an 
input from user as an age. So, check whether the 
number is greater than or equal to 50 or not. If 
user submits the button without
entering age then it shows “The field is empty”.
[The number must be taken from the keyboard by
user] Sample Input and output:
Input Outpu
20 your are not allowed
50 You are allowed
 The field is empty
60 you are allowed
49 You are not allowed
'''

age = int(input('enter the age: '))
if age >=50:
 print("you are allowed")
elif age <= 49:
 print("you are not allowed")
else:
 print("The field is empty")