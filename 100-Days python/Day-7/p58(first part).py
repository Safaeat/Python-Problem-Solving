import random

list = []
list1 = ['apple','banana','orange','malta','kola','lichu']
count = 0
word = random.choice(list1)
print(word)
length = len(word)
guess = input("Guess the word: ")

for index in range(length):
  if guess == word[index]:
    print("Right.")
  else:
    print("Wrong.")










