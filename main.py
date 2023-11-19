import random

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

#Write your code below this line 👇
r_p_s = [rock, paper, scissors]

computer_chose = r_p_s[random.randint(0, 2)]

you_chose = input("What do you choose? type 0 for rock, 1 for paper, 2 for scissors. ")

if you_chose == '0':
  print("You chose:" + r_p_s[0])
elif you_chose == '1':
  print("You chose:" + r_p_s[1])
else:
  print("You chose:" + r_p_s[2])

print("Computer chose:" + computer_chose)

if you_chose == "0" and computer_chose == rock:
  print("Draw!")
if you_chose == "1" and computer_chose == rock:
  print("You win!")
if you_chose == "2" and computer_chose == rock:
  print("You lose!")
if you_chose == "0" and computer_chose == paper:
  print("You lose!")
if you_chose == "1" and computer_chose == paper:
  print("Draw!")
if you_chose == "2" and computer_chose == paper:
  print("You win!")
if you_chose == "0" and computer_chose == scissors:
  print("You win!")
if you_chose == "1" and computer_chose == scissors:
  print("You lose!")
if you_chose == "2" and computer_chose == scissors:
  print("Draw!")
