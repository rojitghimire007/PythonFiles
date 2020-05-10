print("Enter your choice: ")
choice1 = input()
print("***!NO CHEATING***\n\n" * 20)
print("Enter your choice: ")
choice2 = input()

if choice1 == choice2:
	print("draw")
elif choice1 == "paper":
	if choice2 == "rock":
		print("p1 wins")
	elif choice2 == "scissors":
		print("p2 wins")
elif choice1 == "rock":
	if choice2 == "paper":
		print("p2 wins")
	elif choice2 == "scissors":
		print("p1 wins")
elif choice1 == "scissors":
	if choice2 == "paper":
	 	print("p1 wins")
	elif choice2 == "rock":
		print("p2 wins")




