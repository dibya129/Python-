import random

choices = ["rock","paper","scissor"]
user_score = 0 
computer_score = 0 

print(" ===== ROCK , PAPER , SCISSORS =====")

while True :
    user_choice = input("Choose Rock Paper Scissor ( or q to quit )")

    if(user_choice == "q"):
        break

    if user_choice not in choices :
        print("INVALID INPUT TRY AGAIN ")
        continue 

    computer_choice = random.choice(choices)

    print(" You chose ",user_choice)
    print(" Computer chose ",computer_choice)

    if(user_choice==computer_choice):
        print(" Its a Tie !")

    elif(user_choice == "rock" and computer_choice == "scissors") or \
        (user_choice == "paper" and computer_choice == "rock") or \
        (user_choice == "scissors" and computer_choice == "paper"):    

        print(" Congrats you win! ")
        user_score+=1

    else:
        print(" Computer wins!")
        computer_score+=1 

    print("Score : ",user_score,"-",computer_score)

print("\n===== FINAL SCORE =====")
print("You:", user_score)
print("Computer:", computer_score)

if user_score > computer_score:
    print("You won the game!")
elif computer_score > user_score:
    print("Computer won the game!")
else:
    print("The game ended in a tie!")