import random


def roll_dice():
    results = random.randint(1,6)
    print(f"Rolling  {results}")


while True:
    user_input = input("please enter the rolling of the dice (y/n): ")
    if user_input.lower()=="y" :
        roll_dice()
    
    elif user_input.lower()=="n":
        print("thank you for using the dice roller")
        break

    if user_input.lower() not in ["y", "n"]:
        print("Invalid input. Please enter 'y' or 'n'.")