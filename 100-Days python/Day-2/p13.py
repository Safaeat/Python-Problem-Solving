#define by age
age = input("Enter the age:")

if int(age) <= 18:
    print("You can not give the vot.")
elif int(age) >= 18:
    print("You are allow to give the vot.")
else:
    print("Please an integer number.")