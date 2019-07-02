# Rock Paper Scissors Game! -_-
from random import randint

# declaring the player variables and setting value
# changing input to lowercase so "Rock" and "RoCk" becomes "rock"
player = input("Enter Player's choice: ").lower()
# using random.randint() module to generate an int of 0, 1 or 2 for "AI"-player2 choice
rnd_num = randint(0, 2)
if rnd_num == 0:
    computer = "rock"
elif rnd_num == 1:
    computer = "paper"
else:
    computer = "scissors"

# printing the "game move"
print("...rock...")
print("...paper...")
print("...scissors...\n")
print(f"Computer chose {computer}!")
# conditional logic to check and print who wins
if (player and player in ("rock, paper, scissors")) and (computer and computer in ("rock, paper, scissors")):
    if player == computer:
        print(f"Oh {player} vs. {computer}, its a draw!")
    elif player == "rock" and computer == "scissors":
        print(f"{player} beats {computer}! Player wins! :-)")
    elif player == "scissors" and computer == "paper":
        print(f"{player} beats {computer}! Player wins! :-)")
    elif player == "paper" and computer == "rock":
        print(f"{player} beats {computer}! Player wins! :-)")
    else:
        print(f"{computer} beats {player}! Computer wins! :-)")

else:
    print("please put in a valid value!")
