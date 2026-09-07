import random

while True:

    number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100!")

    while True:

        guess = int(input("Guess the number! "))
        attempts += 1

        difference = abs(guess - number)

        if difference == 0:
            print("Correct!")
            print("You got it in", attempts, "attempts!")
            break

        elif difference < 5:
            print("Very Close!")

        elif difference < 15:
            print("Close!")

        else:
            print("Far Away!")

    again = input(" Do you want to play again? (y/n): ")

    if again.lower() != "y":
        print("Thanks for playing!")
        break