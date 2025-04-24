import random
secret_number = random.randint(1, 100)
attempts = 0
print("Choose difficulty: Easy / Medium / Hard")
difficulty = input("Enter difficulty: ").lower()

if difficulty == "easy":
    max_attempts = 10
elif difficulty == "medium":
    max_attempts = 7
elif difficulty == "hard":
    max_attempts = 5
else:
    print("Invalid choice. Defaulting to Easy.")
    max_attempts = 10







while True :
    try:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        if guess < 1 or guess > 100:
            print("Please guess a number within the range.")
            continue
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number!{attempts} attempts.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")


if attempts >= max_attempts:
    print(f"❌ You've run out of attempts. The number was {secret_number}.")
    
# 