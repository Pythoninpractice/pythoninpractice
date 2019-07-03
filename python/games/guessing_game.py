from random import randint

choice = "y"
while choice.lower() == "y":
    number = randint(1, 10)
    while True:
        guessed = int(input("Guess a number between 1 and 10: "))
        if guessed == number:
            print("You guessed it! You won! :-)")
            break
        elif guessed < number:
            print("Too low, try again! ")
        elif guessed > number:
            print("Too high, try again! ")
        else:
            print("Please make a valid entry: ")
    choice = input("Do you want to keep playing? (y/n) ")
    if choice.lower() == "n":
        print("Bye.")
        break
