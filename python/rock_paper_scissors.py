# Rock Paper Scissors Game! -_-

# declaring the player variables and setting value
player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

# printing the "game move"
print("...rock...")
print("...paper...")
print("...Scissors...")

# conditional logic to check and print who wins
if (player1 and player1 in ("rock, paper, scissors")) and (player2 and player2 in ("rock, paper, scissors")):
	print("\nSHOOT!")
	if player1 == player2:
		print("Oh, its a draw!")
	elif player1 == "rock" and player2 == "scissors":
		print("player1 wins! :-)")
	elif player1 == "scissors" and player2 == "paper":
		print("player1 wins! :-)")
	elif player1 == "paper" and player2 == "rock":
		print("player1 wins! :-)")

	else:
		print("player2 wins! :-)")

else:
	print("please put in a valid value!")