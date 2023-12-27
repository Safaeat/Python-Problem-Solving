marks = [45, 65, 88, 90]

print(marks[0])

print(marks[3])

print("\nAll numbers in array:")
for score in marks:
    print(score)

#add in array
marks.append(99)

#the last number in array
print(marks[-1])

#add in mid
marks.insert(2, 30)
print(marks)

#search number in array
print(99 in marks)

#list of length
print(len(marks))