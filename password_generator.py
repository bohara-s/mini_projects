import random
import string

while True:

    length = int(input("Enter the desired password length: "))
    if length < 6:
        print("Password length should be at least 6 characters.")
        continue
 
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(all_chars, k=length))
    print(f"🔐 Your generated password: {password}")

    again = input("Generate another password? (yes/no): ").lower()
    if again == "no":
        print("👋 Goodbye!")
        break