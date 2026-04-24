# Functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is indefined."
    else:
        return a / b

while True:
    print(" Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", add(a, b))

    elif choice == "2":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", subtract(a, b))

    elif choice == "3":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", multiply(a, b))

    elif choice == "4":
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Result:", divide(a, b))

    elif choice == "5":
        print("Exiting calculator. bye bye!")
        break

    else:
        print("Invalid choice. Please try again.")