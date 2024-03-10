import random

stage = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

list = []
list1 = ['apple','banana','orange','malta','kola','lichu']
count = 0
life = 0
word = random.choice(list1)
print(f"Welcome to Hangman show. You have to guess the word to help the people from death.\nThis is a name of bd fruit.")
length = len(word)

while count < length:
    list.extend(['_'])
    count += 1

end_of_game = False
while not end_of_game:
  print(list)
  guess = input("Guess the word: ")

  if guess not in word:
     life += 1
     print(list)
     print(f"You have given {guess} as input, which is incorrect. Now you have {6 - life} lifes.\n"+stage[life])

  for index in range(length):
    if guess == word[index]:
      list[index:index + 1] = guess
      index += 1
    else:
      index += 1

  if '_' not in list:
     end_of_game = True
     print(list)
     print("Congratulations!\nYou win.")

  if life == 6:
     end_of_game = True
     print(list)
     print("Bad luck!\nYou lose.")


