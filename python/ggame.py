import random
random_number = random.randint(1,10)
guess = None


while True:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)
    if guess < random_number:
        print("too low")
    elif guess > random_number:
        print("too high")
    else:
        print("You guessed it right")
        question = input("Do you wanna play it again")
        if question == "y":
            random_number = random.randint(1,10)
            guess = ''
        else:
            print("Thanks for playing")
            break






















