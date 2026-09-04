import random 

while True :
    input(" Press Enter to Roll Dice ")

    dice = random.randint(1,6)
    print("You rolled :", dice)

    again = input("Roll Again ? (y/n):")

    if (again.lower()!="y"):
            print("Thanks For Playing ! ")
            break 
    