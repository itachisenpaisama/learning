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

User_Choice = int(input("What do you choose ? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
PC_Choice = random.randint(0,2)

while True:

    if User_Choice == 0:
        print("You chose rock:")
        print(rock)
        break
    elif User_Choice == 1:
        print("You chose paper:")
        print(paper)
        break
    elif User_Choice == 2:
        print("You chose scissors:")
        print(scissors)
        break
    else:
        print("Invalid input. Try again!")
        User_Choice = int(input("What do you choose ? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
        
if PC_Choice == 0:
    print("Computer chose rock:")
    print(rock)
elif PC_Choice == 1:
    print("Computer chose paper:")
    print(paper)
elif PC_Choice == 2:
    print("Computer chose scissors:")
    print(scissors)

if PC_Choice == User_Choice:
    print("You tied!")
elif PC_Choice == 0 and User_Choice == 1:
    print("You win!")
elif PC_Choice == 0 and User_Choice == 2:
    print("You lose!")
elif PC_Choice == 1 and User_Choice == 0:
    print("You lose!")
elif PC_Choice == 1 and User_Choice == 2:
    print("You win!")
elif PC_Choice == 2 and User_Choice == 0:
    print("You win!")
elif PC_Choice == 2 and User_Choice == 1:
    print("You lose!")


