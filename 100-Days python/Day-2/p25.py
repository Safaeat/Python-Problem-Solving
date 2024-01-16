w = int(input("Inter your body weight:"))
h = float(input("Inter your body height(meter):"))

bmi = w / h**(2)
round(bmi,2)
print("Your BMI is:"+ str(bmi))