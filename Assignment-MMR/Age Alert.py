import PySimpleGUI as sg
age = int(int("Enter your age:"))

if age < 18:
    sg.popup_error("Age must be grater than or equal to 18")