
import random
import time

while True:
    try:
       ask_1 = int(input("How many die you wanna roll? 1/2: "))
    except ValueError:
        print("Enter valid no. 1/2")
        continue

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)


    if ask_1 == 1:
        print("Rolling....")
        time.sleep(1)
        print(f"you rolled a die.\nyou got a {die1}")

    elif ask_1 == 2:
        print("Rolling....")
        time.sleep(1)
        print(f"You rolled a dice.\nyou got a {die1}, {die2} ")
    
    else:
        print("You entered an invalid input.")
        continue



    ask_2 = input("Do you wanna play again? y/n: ").lower()

    if ask_2 == "y":
        continue
    
    elif ask_2 == "n":
        print("Thanks for playing.. ")
        break
    else:
        print("You entered an invalid input ")
        continue

