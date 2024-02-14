marks = input("Input the list of marks(inch): ").split()
for n in range(0, len(marks)):
 marks[n] = int(marks[n])
print(marks)
max = 0
for mark in marks:
  if max < mark:
    max = mark

print(f"The maximum mark in the list is: {max}")