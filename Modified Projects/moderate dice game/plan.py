# Plan
# loop 
    #  ask how many die you  wanna roll

    # if  one  
    # rolls one die 
    # if  two 
    # rolls  both dice 
    # if enter invalid answer
    # print "you enter an invalid no."
    # ask user to roll again (of course dice)    

#basic code looks like this of a dice game
import random  
while True:
    
    play_1 = random.randint(1, 6)
    play_2 = random.randint(1, 6)
    user = (f"you rolled a dice and you got\n {play_1}, {play_2}")

    print(user)

    ask = input("do you want to play again (Yes/No)").lower()

    if ask != "yes":
        print("Thanks for playing")
        break
        
    
    else:
        play_1 = random.randint(1, 6)
        play_2 = random.randint(1, 6)
        print(f"you rolled the dice again and you got\n {play_1}, {play_2}")