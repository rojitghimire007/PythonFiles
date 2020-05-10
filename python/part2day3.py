import random
print ("ROCK PAPER SCISSORS\n" *3)
print("Enter your choice: ")
choice = input().lower()
pick = random.randint(0,2) 

if pick == 0:
	cc = "paper"
elif pick == 1:
	cc = "rock"
else:
	cc ="scissors"
print(f"\nThe computer plays '{cc}'\n")

if cc == choice:
	print ("ITs a draw")
elif cc == "paper" and choice =="rock":
	print("Computer wins")
elif cc == "rock" and choice == "scissors":
	print("computer wins")
elif cc == "scissors" and choice == "paper":
	print("computer wins")
else:
	print("you win")











#0 paper 1 rock 2 scissors
