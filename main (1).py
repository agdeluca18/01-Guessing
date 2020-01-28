import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False

while not quit:
    random_number = random.randint(1,10)
    number = input("Please guess a number: ")
    number = int(number)
    count = 1
    while int(number) != random_number:
        print("Sorry, you did't get it right")
        if number > random_number:
            print("Too high!")
        elif number < random_number:
            print("Too low!")
        number = input("Please guess a number: ")
        number = int(number)
    count = count + 1

    print("Good job!")
    print("You guessed it in {} tries!".format(count))
    play_again = input("Would you like to play again? ")
    if play_again == "yes":
        quit = False
    else:
        quit = True 
        