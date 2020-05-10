import random
print ("ROCK PAPER SCISSORS\n" *3)
pick = random.randint(0,2) 
playerCount = 0
computerCount = 0

while playerCount < 2 and computerCount < 2:
	print ("\nROCK PAPER SCISSORS\n" *3)
	print("Enter your choice: ")
	choice = input().lower()
	if choice == "Quit" or choice == "q":
		break
	pick = random.randint(0,2)
	if pick == 0:
		cc = "paper"
	elif pick == 1:
		cc = "rock"
	else:
		cc ="scissors"
	print(f"\nThe computer plays '{cc}'")

	if cc == choice:
		print ("ITs a draw")
	elif cc == "paper" and choice =="rock":
		print("\nComputer wins\n")
		computerCount += 1
	elif cc == "rock" and choice == "scissors":
		print("\ncomputer wins")
		computerCount += 1
	elif cc == "scissors" and choice == "paper":
		print("\ncomputer wins")
		computerCount += 1
	else:
		print("\nyou win")
		playerCount += 1

print(f"Your final score was: {playerCount}")
print(f"Computer's final score was: {computerCount}")
if playerCount > computerCount:
	print("\nYOU WON!!")
elif computerCount > playerCount:
	print("\nComputer Won")
else:
	print("\nIT IS A TIE")
	











#0 paper 1 rock 2 scissors
