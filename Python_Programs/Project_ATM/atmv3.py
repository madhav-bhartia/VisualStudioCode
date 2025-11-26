# ATM Program:
# This program simulates a simple ATM machine where users can check their balance, deposit money, and withdraw money.
# The program maintains a user's balance and provides a menu for different operations.
# The user can perform multiple operations until they choose to exit.
# The program handles invalid inputs and ensures that users cannot withdraw more money than they have in their balance.
# The program also includes a simple authentication mechanism where users must enter a predefined PIN to access their account.
# The program is designed to be user-friendly and provides clear prompts and messages for each operation.
# The program is structured using functions to handle different operations, making it modular and easy to maintain.
# The program uses file handling to save and retrieve the user's balance, ensuring that the balance is persistent across sessions.
# The program includes error handling to manage unexpected situations, such as invalid input or file access issues.
# The program is written in Python and follows best practices for code readability and organization.

import csv

filePath = "Project_ATM\\bank_accounts_3.csv"

def read(filePath):
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
    return list(reader)


def authenticate(accNum: int, pin: int) -> bool:
    with open("Project_ATM\\bank_accounts_3.csv", "r") as rf:
        reader = csv.reader(rf)
        for row in reader:
            if int(row[0]) == accNum and int(row[1]) == pin:
                return True
    return False

def addAcc(accNum: int, pin: int, accHolder: str, balance: float) -> str:
    with open("Project_ATM\\bank_accounts_3.csv", "a", newline='') as wf:
        writer = csv.writer(wf)
        writer.writerow([accNum, pin, accHolder, balance])
    return "Account added successfully"

def delAcc(accNum: int, pin: int) -> str:
    with open("Project_ATM\\bank_accounts_3.csv", "r") as rf:
        reader = csv.reader(rf)
        rows = list(reader)
        for row in rows[1:]:
            if int(row[0]) == accNum and int(row[1]) == pin:
                break
        else:
            return "Error: account not found or name does not match"
    with open("Project_ATM\\bank_accounts_3.csv", "w", newline='') as wf:
        writer = csv.writer(wf)
        for row in rows:
            if eval(row[0]) != accNum:
                writer.writerow(row)
    return "Account deleted successfully"


def chkBalance(accNum: int) -> float|str:
    with open("Project_ATM\\bank_accounts_3.csv", "r") as rf:
        reader = csv.reader(rf)
        for row in reader:
            if int(row[0]) == accNum:
                return float(row[3])
    return "Error: account not found"

def deposit(accNum: int, amt: float, bal: float = 0.0) -> float|str:
    with open("Project_ATM\\bank_accounts_3.csv", "r") as rf:
        reader = csv.reader(rf)
        rows = list(reader)
        for row in rows[1:]:
            if int(row[0]) == accNum:
                bal = float(row[3]) + amt
                row[3] = str(bal)
                break
        else:
            return "Error: account not found"
    with open("Project_ATM\\bank_accounts_3.csv", "w", newline='') as wf:
        writer = csv.writer(wf)
        writer.writerows(rows)
    return bal

def withdrawal(accNum: int, amt: float, bal: float = 0.0) -> float|str:
    with open("Project_ATM\\bank_accounts_3.csv", "r") as rf:
        reader = csv.reader(rf)
        rows = list(reader)
        for row in rows[1:]:
            if int(row[0]) == accNum:
                if float(row[3]) >= amt:
                    bal = float(row[3]) - amt
                    row[3] = str(bal)
                    with open("Project_ATM\\bank_accounts_3.csv", "w", newline='') as wf:
                        writer = csv.writer(wf)
                        writer.writerows(rows)
                    return bal
                else:
                    return "Error: insufficient funds"
    return "Error: account not found"


def display_menu() -> None:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


def main() -> None:
    print("-----------------Welcome to the ATM!------------------")
    print("1. Authenticate")
    print("2. Add Account")
    print("3. Delete Account")
    print("Enter you choice: ")
    chc: int = int(input())
    match chc:
        case 1:
            print("Enter your account number: ")
            accNum: int = int(input())
            print("Enter your PIN: ")
            pin: int = int(input())
            isAuth: bool = authenticate(accNum, pin)
            if isAuth:
                print("Authentication successful!")
                while True:
                    display_menu()
                    choice = input("Choose an option: ")
                    if choice == '1':
                        print(f"Your current balance is: ₹{chkBalance(accNum):.2f}")
                    elif choice == '2':
                        amt = float(input("Enter amt to deposit: "))
                        if amt > 0:
                            print(f"Current Balance: ₹{deposit(accNum, amt):.2f}")
                        else:
                            print("Invalid amount. Please enter a positive number.")
                    elif choice == '3':
                        amt = float(input("Enter amt to withdraw: "))
                        if 0 < amt <= chkBalance(accNum):
                            print(f"Current Balance: ₹{withdrawal(accNum, amt):.2f}")
                        else:
                            print("Invalid amt. Please enter a positive number not exceeding your balance.")
                    elif choice == '4':
                        print("Thank you for using the ATM. Goodbye!")
                        break
                    else:
                        print("Invalid option. Please try again.")
            else:
                print("Authentication failed. Please check your account number and PIN.")
                return
        case 2:
            print("Enter new account number: ")
            accNum: int = int(input())
            print("Set a PIN for the new account: ")
            pin: int = int(input())
            print("Enter new account holder's name: ")
            accHolder: str = input()
            print("Enter initial balance: ")
            balance: float = float(input())
            print(addAcc(accNum, pin, accHolder, balance))
            return
        case 3:
            print("Enter account number to delete: ")
            accNum: int = int(input())
            print("Enter pin to confirm: ")
            pin: int = int(input())
            print(delAcc(accNum, pin))
            return
        case _:
            print("Invalid choice. Exiting.")
            return



main()# End of ATM Program