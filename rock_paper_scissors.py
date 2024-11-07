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

computer_selection = random.choice([rock, paper, scissors])

selection = input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n ")
if selection == "0":
    print(rock)
    print(f"Computer chose: {computer_selection}")
    if computer_selection == rock:
        print("It's a tie")
    elif computer_selection == scissors:
        print("You Win")
    else:
        print("You lose")
elif selection == "1":
    print(paper)
    print(f"Computer chose: {computer_selection})")
    if computer_selection == paper:
        print("It's a tie")
    elif computer_selection == rock:
        print("You Win")
    else:
        print("You lose")
elif selection == "2":
    print(scissors)
    print(f"Computer chose: {computer_selection})")
    if computer_selection == scissors:
        print("It's a tie")
    elif computer_selection == paper:
        print("You Win")
    else:
        print("You lose")