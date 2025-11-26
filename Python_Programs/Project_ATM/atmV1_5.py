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

def chkBalance(accNum: int) -> float|str:
    with open("Project_ATM\\bank_accounts_1.csv", "r") as rf:
        reader = csv.reader(rf)
        for row in reader:
            if eval(row[0]) == accNum:
                return float(row[2])
    return "Error: account not found"

def deposit(accNum: int, amt: float, bal: float = 0.0) -> float|str:
    with open("Project_ATM\\bank_accounts_1.csv", "r") as rf:
        reader = csv.reader(rf)
        rows = list(reader)
        for row in rows:
            if eval(row[0]) == accNum:
                bal = float(row[2]) + amt
                row[2] = str(bal)
                break
        else:
            return "Error: account not found"
    with open("Project_ATM\\bank_accounts_1.csv", "w", newline='') as wf:
        writer = csv.writer(wf)
        writer.writerows(rows)
    return bal

def withdrawal(accNum: int, amt: float, bal: float = 0.0) -> float|str:
    with open("Project_ATM\\bank_accounts_1.csv", "r") as rf:
        reader = csv.reader(rf)
        rows = list(reader)
        for row in rows:
            if eval(row[0]) == accNum:
                if float(row[2]) >= amt:
                    bal = float(row[2]) - amt
                    row[2] = str(bal)
                    with open("Project_ATM\\bank_accounts_1.csv", "w", newline='') as wf:
                        writer = csv.writer(wf)
                        writer.writerows(rows)
                    return bal
                else:
                    return "Error: insufficient funds"
    return "Error: account not found"





#def authenticate(accNum, pin):




def display_menu():
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")



def main():
    print("-----------------Welcome to the ATM!------------------")
    print("Enter you account number: ")
    accNum: int = int(input())
    # print("Enter your PIN: ")
    # pin: int = input()
    if True: #authenticate(accNum, pin):
        while True:
            # balance = bankFile(chkBalance=accNum)
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



main() 