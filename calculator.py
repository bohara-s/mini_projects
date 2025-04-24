def calculater():
    print("welcome to calculater program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")

    choice = input("enter a choice (1-5): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice =='1':
            result = num1 + num2
            print(f"The result of addition is: {result}")

        elif choice == '2': 
            result = num1 - num2
            print(f"The result of subtraction is: {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"The result of multiplication is: {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"The result of division is: {result}")
            else:
                print("Error! Division by zero.")
        elif choice == '5':
            result = num1 % num2
            print(f"The result of modulus is: {result}")
    else:
        print("Invalid choice! Please select a valid option.")

calculater()