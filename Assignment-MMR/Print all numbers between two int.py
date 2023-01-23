'''
 a Python program that will take two 
interger umber from user. if user put first 
number 4 and second number 9 then print the 
value 4 5 6 7 8 9. Note: first number is always 
smaller than second number .if user put first 
number large and second number small then it 
will alert the message(“Please give first number 
small and second number large”).
'''


import PySimpleGUI as sg
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2:
 for i in range(num1, num2+1):
   print(i)
else:
 sg.popup_error("Please give first number small and second number large")
