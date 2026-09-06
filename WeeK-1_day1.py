# Simple ATM Program

balance = 5000


def check_balance():
    print("Your balance is:", balance, "SAR")


def deposit():
    global balance

    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Deposit successful")
        print("New balance:", balance, "SAR")
    else:
        print("Invalid amount")


def withdraw():
    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")

    elif amount > balance:
        print("Insufficient balance")

    else:
        balance = balance - amount
        print("Withdrawal successful")
        print("Remaining balance:", balance, "SAR")


def atm():
    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("Thank you for using the ATM")
            break

        else:
            print("Invalid choice. Please try again.")


atm()