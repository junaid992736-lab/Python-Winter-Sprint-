
FILE_NAME = "bank.txt"

def save_account(name, balance):
    with open(FILE_NAME, "w") as file:
        file.write(name + "\n")
        file.write(str(balance))



def read_account():
    with open(FILE_NAME, "r") as file:
        name = file.readline().strip()
        balance = int(file.readline().strip())
    return name, balance



def deposit(balance):
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Amount deposited successfully.")
    return balance



def withdraw(balance):
    amount = int(input("Enter withdrawal amount: "))
    if amount <= balance:
        balance -= amount
        print("Withdrawal successful.")
    else:
        print("Insufficient balance.")
    return balance


def menu(balance):
    print("\nChoose operation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        balance = deposit(balance)
        save_account(name, balance)
        menu(balance)

    elif choice == "2":
        balance = withdraw(balance)
        save_account(name, balance)
        menu(balance)

    elif choice == "3":
        return

    else:
        print("Invalid choice.")
        menu(balance)

name = input("Enter account holder name: ")
balance = int(input("Enter initial balance: "))

save_account(name, balance)
menu(balance)


name, balance = read_account()
print("\n--- ACCOUNT SUMMARY ---")
print("Account Holder:", name)
print("Final Balance: ₹", balance)