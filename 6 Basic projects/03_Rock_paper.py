# import random
 # every thing will be in loop
        # ask a user to choose between (r/p/s):

        # now computer will choose

        # now decide who wins

        # if user choose something else print please slect a valid choice

        # now ask  form user that he/she wanna continue or not 
# My code and proud of it no fully satisfied but ok 
 
# while True:
#     ask = input("rock, paper or scissor ?(r/p/s)").lower()

#     options = ("r", "p", "s")
#     computer = random.choice(options)

#     if computer =="r" and ask == "p":
#         print(f"computer choose:{computer}\nyou win!!!...")

#     elif computer =="p" and ask =="r":
#         print(f"computer choose:{computer}\nunfortunately you loose!!!!...")

#     elif computer =="p" and ask == "s":
#         print(f"computer choose:{computer}\nyou winn..")

#     elif computer =="s" and ask == "p":
#         print(f"computer choose:{computer}\nyou loose")

#     elif computer =="r" and ask == "s":
#         print(f"computer choose:{computer}\nyou loose")

#     elif computer =="s" and ask == "r":
#         print(f"computer choose:{computer}\nyou win")

#     else:
#         print(f"computer choose:{computer}\nplease enter a valid response")
    
#     again= input("are you still wana continue(y/n): ").lower()
#     if again =="y":
#         continue

#     elif again=="n":
#         break
#     else:
#         print("please enter a valid choice")



#solution-1
# Ask the user to make the choice
# if choice is not valid
#    print an error

# let the computer make a choice
# print choices("emojis")
# determine the winner
# Ask the user if they wanna continue
# if not 
# terminate
import random

emojis = {"r": "🪨", "s": "✂️", "p": "📃"}
choices = ("r", "p","s")
while True:
        user_choice = input("Rock, Paper, Scissor? (r/p/s: )").lower()
        if user_choice not in choices:
            print("invalid choice")
            continue

        computer_choice= random.choice(choices)

        print(f"you chose {emojis[user_choice]}")
        print(f"computer chose {emojis[computer_choice]}")

        if user_choice == computer_choice:
            print("Tie!")

        elif(
            (user_choice=="r" and computer_choice == "s")or
            (user_choice=="s" and computer_choice == "p")or
            (user_choice=="p" and computer_choice == "r")):
            print("you win")

        else:
            print("you lose")

        should_continue = input("continue? (y/n): ").lower()
        if should_continue == "n":
            break