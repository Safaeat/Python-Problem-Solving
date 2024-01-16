first = input("Enter 1st number:")
second = input("Enter 2nd number:")
op = input("Enter the operator(+,-,*,/,%):")

first = int(first)
second = int(second)

if op == "+":
    print(first + second)
elif op == "-":
    print(first - second)
elif op == "*":
    print(first * second)
elif op == "%":
    print(first % second)
else:
    print("Wrong input.")