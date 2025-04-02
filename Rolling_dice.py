import random
'''
while True:
    
    play = random.randint(1, 6)
    user = (f"you rolled a dice and you got\n {play}")

    print(user)

    saga = input("do you want to play again (Yes/No)").lower()

    if saga != "yes":
        print("Thanks for playing")
        break
        
    
    else:
       
        print(f"you rolled the dice again and you got\n {play}")


#solution
while True: 
    enters =input("Role the dice?: ") .lower()
    if enters == "y":
        die1= random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
    elif enters == "n":
        print("thankyou for playing") # print thank you 
        break # terminate the game 
    else: # else
        print("invalid choice") # print invalid choice



# modified code
# adding a fuction which specify how many dice you wanna roll
'''
# solution

        
'''
    # else:
    #     break
    def choice2():    
        choice2 = input("Are you wanna play again") .lower()
        if choice2=="n":
            print ("Thanks for playing...") 
            break
        elif choice2 == "y":
            print() 
        else:
            print("your out put is invalid, try again")    
    choice1 =input("How much die you wanna role 1🎲or 2🎲🎲?: ") .lower() #ask : you wanna roll that dice
    die1 = (random.randint(1, 6)) # ask user how many die he wanana thorw 
    die2 = random.randint(1, 6)
    if  choice1==1:
        print(die1)
    elif choice1==2:
        print(die1, die2)'''

import random

while True:
    def choice0():
            choice1 = random.randint
            print(choice1) 


    def choice():
        choice1 = random.randint(1, 6)
        choice2 = random.randint(1,6)
        print(choice1, choice2)

    enter = input("How much dice you wanna role?: ").lower()
    
    if enter =="n":
         print("Thanks for playing")
    
    
    if enter ==1:
        choice0()

    elif enter ==2:
        choice()

    
    else:
        print("you entered an invalid input")

