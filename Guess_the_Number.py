import random

Computer_guess = random.randrange(1, 100)
# print(Computer_guess)
user_guess = None
no_of_guesses = 0

while (Computer_guess != user_guess):
    user_guess = int(input("Enter Your Guess:"))

    if Computer_guess == user_guess:
        print("Your Guess is Right!!")
    else:
        if Computer_guess > user_guess:
            print("Go for Higher Number..")
        else:
            print("Go for Lower NUmber..")

    no_of_guesses += 1
print(f"You Guess number in {no_of_guesses} guesses")

if no_of_guesses > 10:
    print("Your Guessing Skills are Poor")
else:
    print("Your Guessing Skills are Excellent!! ")
