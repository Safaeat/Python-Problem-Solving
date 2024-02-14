import random
print("Lets play Rock, Paper, Scissers.")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choose = int (input("0 for Rock, 1 for Paper and 2 for Scissers: "))
if choose >= 3 or choose < 0:
    print("You typed an invalid number, you lose!")
else:
    random1 = random.randint(0, 2)
    img = [rock, paper, scissors]

    if choose == random1:
      print(f"You choose:"+img[choose]+"Random generate is"+img[random1]+"It's draw!")
    elif choose == 0 and random1 == 1:
      print(f"You choose:"+img[choose]+"Random generate is"+img[random1]+"You lose!")
    elif choose == 0 and random1 == 2:
      print(f"You choose:"+img[choose]+"Random generate is"+img[random1]+"You win!")
    elif choose == 1 and random1 == 2:
      print(f"You choose:"+img[choose]+"Random generate is"+img[random1]+"You lose!")
    elif (choose == 1) and (random1 == 0):
      print(f"You choose:"+img[choose]+"Random generate is"+img[random1]+"You win!")
    elif (choose == 2) and (random1 == 0):
      print(f"You choose:"+img[choose]+"Random generate is"+img[random1]+"You lose!")
    elif (choose == 2) and (random1 == 1):
      print(f"You choose:"+img[choose]+"Random generate is"+img[random1]+"You win!")