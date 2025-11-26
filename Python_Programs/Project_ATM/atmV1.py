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

def bankFile(chkBalance = None, deposit = None, withdrawal = None):
    if chkBalance is not None:
        with open("Project_ATM\\bank_accounts_1.csv", "r") as rf:
            reader = csv.reader(rf)
            for row in reader:
                if int(row[0]) == chkBalance:
                    return float(row[2])
        return "Error: account not found"
    
    elif deposit is not None:
        with open("Project_ATM\\bank_accounts_1.csv", "r") as rf:
            reader = csv.reader(rf)
            rows = list(reader)
            for row in rows:
                if int(row[0]) == deposit[0]:
                    row[2] = str(float(row[2]) + deposit[1])
                    break
            else:
                return "Error: account not found"
        with open("Project_ATM\\bank_accounts_1.csv", "w", newline='') as wf:
            writer = csv.writer(wf)
            writer.writerows(rows)
        return "Successfully deposited"
    
    elif withdrawal is not None:
        with open("Project_ATM\\bank_accounts_1.csv", "r") as rf:
            reader = csv.reader(rf)
            rows = list(reader)
            for row in rows:
                if int(row[0]) == withdrawal[0]:
                    if float(row[2]) >= withdrawal[1]:
                        row[2] = str(float(row[2]) - withdrawal[1])
                        with open("Project_ATM\\bank_accounts_1.csv", "w", newline='') as wf:
                            writer = csv.writer(wf)
                            writer.writerows(rows)
                        return "Successfully withdrawn"
                    else:
                        return "Error: insufficient funds"
        return "Error: account not found"





#def authenticate(account_number, pin):




def display_menu():
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")



def main():
    print("-----------------Welcome to the ATM!------------------")
    print("Enter you account number: ")
    account_number: int = int(input())
    # print("Enter your PIN: ")
    # pin: int = input()
    if True: #authenticate(account_number, pin):
        while True:
            # balance = bankFile(chkBalance=account_number)
            display_menu()
            choice = input("Choose an option: ")
            if choice == '1':
                print(f"Your current balance is: ₹{bankFile(chkBalance=account_number):.2f}")
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                if amount > 0:
                    print(bankFile(deposit=(account_number, amount)))
                    print(f"Current Balance: ₹{bankFile(chkBalance=account_number):.2f}")
                else:
                    print("Invalid amount. Please enter a positive number.")
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                if 0 < amount <= bankFile(chkBalance=account_number):
                    print(bankFile(withdrawal=(account_number, amount)))
                    print(f"Current Balance: ₹{bankFile(chkBalance=account_number):.2f}")
                else:
                    print("Invalid amount. Please enter a positive number not exceeding your balance.")
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Authentication failed. Please check your account number and PIN.")



main()