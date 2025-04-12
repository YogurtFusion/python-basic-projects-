import random
'''
my code

while True:
    
    play = random.randint(1, 6)
    user = (f"you rolled a dice and you got\n {play}")

    print(user)

    ask = input("do you want to play again (Yes/No)").lower()

    if ask != "yes":
        print("Thanks for playing")
        break
        
    
    else:
       
        print(f"you rolled the dice again and you got\n {play}")

'''
#solution
while True: 
    user_enters =input("Role the dice? y/n: ") .lower()
    if user_enters == "y":
        die1= random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"you got {die1} and {die2}")
    elif user_enters == "n":
        print("thankyou for playing")  
        break 
    else: 
        print("invalid choice") 