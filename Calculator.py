# Calculator

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


calc_message = "Available operations: 1. Add, 2. Subtract, 3. Multiply, 4. Divide "

while True:
    # Take in user input
    user_choice = input("Please choose a number 1/2/3/4: ")

    # Check if valid input
    if user_choice in ('1', '2', '3', '4'):
        first_num = float(input("Please enter first number: "))
        second_num = float(input("Please enter second number: "))
        if user_choice == '1':
            print(f"{first_num} + {second_num} = {add(first_num, second_num)}")
        elif user_choice == '2':
            print(f"{first_num} - {second_num} = {subtract(first_num, second_num)}")
        elif user_choice == '3':
            print(f"{first_num} * {second_num} = {multiply(first_num, second_num)}")
        elif user_choice == '4':
            print(f"{first_num} / {second_num} = {divide(first_num, second_num)}")

        # Check if user wants to continue
        # If no, break
        new_expression = input("Would you like to continue with another expression? (yes/no): ")
        if new_expression == 'no':
            break

    # If invalid input
    else:
        print("Invalid input.")