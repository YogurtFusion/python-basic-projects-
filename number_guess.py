import random

random_no = (random.randint(1, 100))
while True:
    try:
        guess = int(input("enter no. between 1 to 100: "))

        if guess < random_no:
            print("Too low! try again")

        elif guess > random_no:
            print("Too High! Try again")


        else:
            print("You guessed a right no. congrats")
            break
    except ValueError:
     print("please entejr a valid no. ")
    
