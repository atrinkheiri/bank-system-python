import random
import json
import os

def load_accounts():
    if os.path.exists("accounts.json"):
        with open("accounts.json", "r") as file:
            return json.load(file)
    else:

        return [
            {"Card number": 5894631226873586, "Balance": 100000, "Active": True},
            {"Card number": 9876543210123456, "Balance": 50000, "Active": True},
            {"Card number": 1234567890123456, "Balance": 75000, "Active": True},
            {"Card number": 2222333344445555, "Balance": 250000, "Active": True},
            {"Card number": 3333444455556666, "Balance": 300000, "Active": True},
            {"Card number": 4444555566667777, "Balance": 150000, "Active": True},
            {"Card number": 5555666677778888, "Balance": 120000, "Active": True},
            {"Card number": 6666777788889999, "Balance": 90000, "Active": True}
        ]

def save_accounts(accounts):
    with open("accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)

def show_menu():
    print("\nWelcome to the Bank System!\n"
          "1.Open Account\n"
          "2.Deposit Money\n"
          "3.Withdraw Money\n"
          "4.Close Account\n"
          "5.Display Account\n"
          "6.See active accounts with the highest balance\n"
          "0.Exit\n")

def find_account(accounts):
    user_cardnumber = input("Enter your bank account number: ")
    while len(user_cardnumber) != 16 or not user_cardnumber.isdigit():
        print("The number of digits is not acceptable")
        user_cardnumber = input("Enter your bank account number: ")
    user_cardnumber = int(user_cardnumber)
    for user_account in accounts:
        if user_account["Card number"] == user_cardnumber:
            return user_account
    print("Card number not found")
    return None


accounts = load_accounts()

while True:
    show_menu()
    choice_input = input("Enter your choice: ")
    while not choice_input.isdigit() or int(choice_input) < 0 or int(choice_input) > 6:
        print("Error! Please enter numbers between 0 and 6")
        show_menu()
        choice_input = input("Enter your choice: ")
    choice = int(choice_input)

    if choice == 1:
        name = input("Enter your name: ")
        familyname = input("Enter your family name: ")
        gender = input("Enter your gender: ")
        age = int(input("Enter your age: "))
        while age < 0:
            print("The age is not correct, be careful")
            age = int(input("Enter your age: "))
        while gender != "woman" and gender != "man":
            print("Error!/ try again")
            gender = input("Enter your gender: ")
        balance = 0
        card_number = random.randint(1000000000000000, 9999999999999999)
        print("Account number for you:", card_number)
        user_account = {
            "Name": name,
            "Family name": familyname,
            "Gender": gender,
            "Age": age,
            "Card number": card_number,
            "Balance": balance,
            "Active": True
        }
        accounts.append(user_account)
        save_accounts(accounts)

    elif choice == 2:
        user_account = find_account(accounts)
        if user_account:
            if user_account["Active"]:
                amount = int(input("Enter the deposit amount: "))
                while amount <= 0:
                    print("The amount must be positive")
                    amount = int(input("Enter the deposit amount: "))
                balance_now = user_account["Balance"]
                user_account["Balance"] += amount
                print("The deposit was successful")
                print("Previous inventory:", balance_now)
                print("New inventory:", user_account["Balance"])
                save_accounts(accounts)
            else:
                print("This account is inactive")

    elif choice == 3:
        user_account = find_account(accounts)
        if user_account:
            if user_account["Active"]:
                amount = int(input("Enter the withdrawal amount: "))
                while amount <= 0:
                    print("The amount must be positive")
                    amount = int(input("Enter the withdrawal amount: "))
                balance_now = user_account["Balance"]
                if amount > balance_now:
                    print("There is not enough inventory")
                else:
                    user_account["Balance"] -= amount
                    print("The withdrawal was successful")
                    print("Your new inventory:", user_account["Balance"])
                    save_accounts(accounts)
            else:
                print("This account is inactive")

    elif choice == 4:
        user_account = find_account(accounts)
        if user_account:
            if user_account["Active"]:
                confirm = input("Are you closing your account? ")
                if confirm.lower() == "yes":
                    user_account["Active"] = False
                    print("The account was closed successfully")
                    save_accounts(accounts)
                else:
                    print("Account closure operation canceled")
            else:
                print("This account has already been deactivated")

    elif choice == 5:
        user_account = find_account(accounts)
        if user_account:
            if user_account["Active"]:
                print("Your account information:")
                print("Card number:", user_account["Card number"])
                print("Inventory:", user_account["Balance"])
                print("Status: Active")
            else:
                print("This account is inactive")

    elif choice == 6:

        top_accounts = sorted(accounts, key=lambda x: x["Balance"], reverse=True)[:5]
        print("Five accounts with the highest balance:")
        for acc in top_accounts:
            print("Card number:", acc["Card number"], "| Inventory:", acc["Balance"])

    elif choice == 0:
        print("Goodbye!")
        save_accounts(accounts)
        break
