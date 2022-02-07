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

choices = [rock,paper,scissors]
your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
print(choices[your_choice])
print("Computer choice:")
pc_choice = random.choice(choices)
print(pc_choice)
if your_choice == 0:
  if pc_choice == rock:
    print('draw')
  elif pc_choice == paper:
    print('you lost')
  elif pc_choice == scissors:
    print('you won')
elif your_choice == 1:
  if pc_choice == rock:
    print('you won')
  elif pc_choice == paper:
    print('draw')
  elif pc_choice == scissors:
    print('you lost')
elif your_choice == 2:
  if pc_choice == rock:
    print('you lost')
  elif pc_choice == paper:
    print('you won')
  elif pc_choice == scissors:
    print('draw')