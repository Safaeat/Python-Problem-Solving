sum = 0

while True:
    a = int(input("Enter your numbers: "))

    if a <= 10:
        sum += a
    else:
        break

print(f"Total sum = {sum}")
