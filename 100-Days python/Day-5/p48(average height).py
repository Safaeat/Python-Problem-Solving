heights = input("Input the list of heights(inch): ").split()
numbers = 0
sum = 0

for height in heights:
 sum += int(height)
 numbers += 1
average = sum / numbers

print(f"The average of heights is: {average} inch")
