import random

list = []
list1 = ['apple','banana','orange','malta','kola','lichu']
count = 0
word = random.choice(list1)
print(f"The ans is : "+word)
length = len(word)

while count < length:
    list.extend(['_'])
    count += 1

guess = input("Guess the word: ")

for index in range(length):
  if guess == word[index]:
    list[index:index + 1] = guess
    index += 1
  else:
    index += 1

print(list)
