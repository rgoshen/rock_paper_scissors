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

hand_images = [rock, paper, scissors]

welcome_msg = '''
Welcome to the rock, paper, scissors game.
Rules: Type '0' for rock, '1' for paper or '2' for scissors.
'''
print(welcome_msg)
human_player = int(input("What do you choose?\n"))

if human_player < 0 or human_player > 2:
    print("You typed an invalid number, you lose!")
else:
    print("You chose: " + hand_images[human_player])
    computer_player = random.randint(0, 2)
    print("Computer chose: " + hand_images[computer_player])
    if human_player == 0 and computer_player == 1:
        print("You lose!")
    elif human_player == 1 and computer_player == 2:
        print("You lose!")
    elif human_player == 2 and computer_player == 0:
        print("You lose!")
    elif human_player == computer_player:
        print("It's a draw.")
    else:
        print("You Win!")
