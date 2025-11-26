import csv
import os

CSV_FILE = "Project_ATM\\bank_accounts_ai.csv"
HEADERS = ["AccountNumber", "PIN", "Holder", "Balance"]

# ---------- Utility Functions ----------

def init_csv():
    """Ensure the CSV file exists with headers."""
    if not os.path.exists(CSV_FILE):
        os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
        with open(CSV_FILE, "w", newline='') as wf:
            writer = csv.writer(wf)
            writer.writerow(HEADERS)

def read_accounts():
    """Read all accounts from CSV as a list of lists."""
    with open(CSV_FILE, "r", newline='') as rf:
        reader = csv.reader(rf)
        return list(reader)

def write_accounts(rows):
    """Write all accounts back to CSV."""
    with open(CSV_FILE, "w", newline='') as wf:
        writer = csv.writer(wf)
        writer.writerows(rows)

# ---------- Core ATM Functions ----------

def authenticate(accNum: int, pin: int) -> bool:
    rows = read_accounts()
    for row in rows[1:]:
        if int(row[0]) == accNum and int(row[1]) == pin:
            return True
    return False

def add_account(accNum: int, pin: int, accHolder: str, balance: float) -> str:
    rows = read_accounts()
    for row in rows[1:]:
        if int(row[0]) == accNum:
            return "Error: Account number already exists."
    rows.append([accNum, pin, accHolder, balance])
    write_accounts(rows)
    return "Account added successfully."

def delete_account(accNum: int, pin: int) -> str:
    rows = read_accounts()
    for i, row in enumerate(rows[1:], start=1):
        if int(row[0]) == accNum and int(row[1]) == pin:
            del rows[i]
            write_accounts(rows)
            return "Account deleted successfully."
    return "Error: account not found or PIN incorrect."

def check_balance(accNum: int):
    rows = read_accounts()
    for row in rows[1:]:
        if int(row[0]) == accNum:
            return float(row[3])
    return "Error: account not found."

def deposit(accNum: int, amt: float):
    rows = read_accounts()
    for row in rows[1:]:
        if int(row[0]) == accNum:
            row[3] = str(float(row[3]) + amt)
            write_accounts(rows)
            return float(row[3])
    return "Error: account not found."

def withdraw(accNum: int, amt: float):
    rows = read_accounts()
    for row in rows[1:]:
        if int(row[0]) == accNum:
            bal = float(row[3])
            if bal >= amt:
                row[3] = str(bal - amt)
                write_accounts(rows)
                return float(row[3])
            else:
                return "Error: insufficient funds."
    return "Error: account not found."

# ---------- Menu Functions ----------

def display_main_menu():
    print("\n--- Welcome to the ATM ---")
    print("1. Authenticate")
    print("2. Add Account")
    print("3. Delete Account")
    print("4. Exit")

def display_account_menu():
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Logout")

# ---------- Main Program ----------

def main():
    init_csv()

    while True:
        display_main_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            try:
                accNum = int(input("Enter account number: "))
                pin = int(input("Enter PIN: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if authenticate(accNum, pin):
                print("Authentication successful!")
                while True:
                    display_account_menu()
                    sub_choice = input("Choose an option: ")

                    if sub_choice == '1':
                        bal = check_balance(accNum)
                        if isinstance(bal, float):
                            print(f"Your current balance is: ₹{bal:.2f}")
                        else:
                            print(bal)

                    elif sub_choice == '2':
                        try:
                            amt = float(input("Enter amount to deposit: "))
                            if amt <= 0:
                                print("Amount must be positive.")
                                continue
                        except ValueError:
                            print("Invalid amount.")
                            continue
                        bal = deposit(accNum, amt)
                        print(f"Current Balance: ₹{bal:.2f}" if isinstance(bal, float) else bal)

                    elif sub_choice == '3':
                        try:
                            amt = float(input("Enter amount to withdraw: "))
                            if amt <= 0:
                                print("Amount must be positive.")
                                continue
                        except ValueError:
                            print("Invalid amount.")
                            continue
                        bal = withdraw(accNum, amt)
                        print(f"Current Balance: ₹{bal:.2f}" if isinstance(bal, float) else bal)

                    elif sub_choice == '4':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")

            else:
                print("Authentication failed.")

        elif choice == 2:
            try:
                accNum = int(input("Enter new account number: "))
                pin = int(input("Set a PIN: "))
                accHolder = input("Enter account holder's name: ")
                balance = float(input("Enter initial balance: "))
            except ValueError:
                print("Invalid input.")
                continue
            print(add_account(accNum, pin, accHolder, balance))

        elif choice == 3:
            try:
                accNum = int(input("Enter account number to delete: "))
                pin = int(input("Enter PIN to confirm: "))
            except ValueError:
                print("Invalid input.")
                continue
            print(delete_account(accNum, pin))

        elif choice == 4:
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()