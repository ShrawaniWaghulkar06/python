"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def menu():
    print("\n--- CALC Menu ---")
    print("a) Addition")
    print("b) Subtraction")
    print("c) Multiplication")
    print("d) Division")
    print("e) Modulus")
    print("q) Quit")

while True:
    menu()
    choice = input("Select an option: ").lower()

    if choice == 'q':
        print("Exiting CALC. Goodbye!")
        break

    if choice in ['a', 'b', 'c', 'd', 'e']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 'a':
            print(f"Result: {add(num1, num2)}")
        elif choice == 'b':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == 'c':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == 'd':
            print(f"Result: {divide(num1, num2)}")
        elif choice == 'e':
            print(f"Result: {modulus(num1, num2)}")
    else:
        print("Invalid choice! Please try again.")
        """
balance = 0.0  # Initial Balance


def display_balance():
    print(f"\nCurrent Balance: ${balance:.2f}")


def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Successfully deposited ${amount:.2f}")
    else:
        print("Invalid amount!")


def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if 0 < amount <= balance:
        balance -= amount
        print(f"Successfully withdrew ${amount:.2f}")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        print("Invalid amount!")


def bank_menu():
    while True:
        print("\n--- Bank Account Menu ---")
        print("a) Display Balance")
        print("b) Deposit Money")
        print("c) Withdraw Money")
        print("q) Exit")

        choice = input("Select an option: ").lower()

        if choice == 'a':
            display_balance()
        elif choice == 'b':
            deposit()
        elif choice == 'c':
            withdraw()
        elif choice == 'q':
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid selection.")


# Run the bank program
bank_menu()

