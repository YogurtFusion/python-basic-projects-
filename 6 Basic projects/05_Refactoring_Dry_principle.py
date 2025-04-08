# Dry is a priniciple of programing which means:
# Don't Repeat Yourself

import random

Rock = "r"
Scissors = "s"
Paper ="p"
emojis = {Rock: "🪨", Scissors: "✂️", Paper: "📃"}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, Paper or scissors? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"you choose {emojis[user_choice]}")
    print(f"computer chose {emojis[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")

    elif(
        (user_choice == Rock and computer_choice == Scissors) or
        
        (user_choice == Scissors and computer_choice == Paper) or
        
        (user_choice == Paper and computer_choice == Rock)):
        print("YOU WIN!!!")
        
    else:
        print("you lose")

def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)
        
        determine_winner(user_choice, computer_choice)
        
        should_continue = input("continue? (y/n): ").lower()
        if should_continue == "n":
            print("Thanks for playing!!...")
            break



play_game()

# import random

# ROCK = 'r'
# SCISSORS = 's'
# PAPER = 'p'
# emojis = { ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
# choices = tuple(emojis.keys())

# def get_user_choice():
#   while True:
#     user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
#     if user_choice in choices:
#       return user_choice      
#     else:
#       print('Invalid choice!')
      
# def display_choices(user_choice, computer_choice):
#   print(f'You chose {emojis[user_choice]}')
#   print(f'Computer chose {emojis[computer_choice]}')


# def determine_winner(user_choice, computer_choice):
#   if user_choice == computer_choice:
#     print('Tie!')
#   elif (
#     (user_choice == ROCK and computer_choice == SCISSORS) or 
#     (user_choice == SCISSORS and computer_choice == PAPER) or 
#     (user_choice == PAPER and computer_choice == ROCK)):
#     print('You win')
#   else:
#     print('You lose')  

# def play_game():
#   while True:
#     user_choice = get_user_choice()

#     computer_choice = random.choice(choices)

#     display_choices(user_choice, computer_choice)

#     determine_winner(user_choice, computer_choice)

#     should_continue = input('Continue? (y/n): ').lower()
#     if should_continue == 'n':
#       break


# play_game()
