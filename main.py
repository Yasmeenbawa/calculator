print("Welcome here!")
user_name = input("What is your name?")


def add(a, b):
    print(a + b)


def subtract(a, b):
    print(a - b)


def multiply(a, b):
    print(a * b)


def divide(a, b):
    print(a / b)

calculator_on = True

while calculator_on:

    user_choice = int(input(f"hello {user_name}, type 1 to add, 2 to subtract, 3 to multiply, "
                            f"4 to divide and 5 to exit?"))

    if user_choice == 1 or user_choice == 2 or user_choice == 3 or user_choice == 4:
        first_number = int(input("Enter your first number"))
        second_number = int(input("Enter your second number"))
        if user_choice == 1:
            add(first_number, second_number)
        elif user_choice == 2:
            subtract(first_number, second_number)
        elif user_choice == 3:
            multiply(first_number, second_number)
        elif user_choice == 4:
            divide(first_number, second_number)
        # else:
        #     print("Goodbye")
    elif user_choice == 5:
        print(f"Goodbye {user_name}")
        calculator_on = False
    else:
        print("Operation doesnt exist!")
