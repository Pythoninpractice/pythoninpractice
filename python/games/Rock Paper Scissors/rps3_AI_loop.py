# Rock Paper Scissors Game! -_-
from random import randint

player_score = 0
computer_score = 0

while True:
    # declaring the player variables and setting value
    # changing input to lowercase so "Rock" and "RoCk" becomes "rock"
    print("\n___--- Rock Paper Scissors - The Game ---___")
    print(f"\nPlayer:{player_score} Computer:{computer_score}")
    player = input("\nChoose> rock, paper, scissors or exit: ").lower()
    if player == "exit":
        break
    # using random.randint() module to generate an int of 0, 1 or 2 for "AI"-player2 choice
    rnd_num = randint(0, 2)
    if rnd_num == 0:
        computer = "rock"
    elif rnd_num == 1:
        computer = "paper"
    else:
        computer = "scissors"

    # conditional logic to check and print who wins
    if (player and player in ("rock, paper, scissors")) and (computer and computer in ("rock, paper, scissors")):
        # printing the actual score

        # printing the "game move"
        print("...rock...")
        print("...paper...")
        print("...scissors...\n")
        print(f"Computer chose {computer}!")
        if player == computer:
            print(f"Oh {player} vs. {computer}, its a draw!")
        elif player == "rock" and computer == "scissors":
            print(f"{player} beats {computer}! Player wins! :-)")
            player_score += 1
        elif player == "scissors" and computer == "paper":
            print(f"{player} beats {computer}! Player wins! :-)")
            player_score += 1
        elif player == "paper" and computer == "rock":
            print(f"{player} beats {computer}! Player wins! :-)")
            player_score += 1
        else:
            print(f"{computer} beats {player}! Computer wins! :-)")
            computer_score += 1
    else:
        print("please put in a valid value!")
