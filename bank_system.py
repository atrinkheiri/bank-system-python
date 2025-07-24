import random
def show_menu():
    print("Welcome to the Bank System!\n"
          "1.Open Account\n"
          "2.Deposit Money\n"
          "3.Withdraw Money\n"
          "4.Close Account\n"
          "5.Display Account\n"
          "6.See active accounts with the highest balance\n"
          "0.Exit\n")
def find_account(accounts):
    user_cardnumber = input("Enter your bank account number:")
    while len(user_cardnumber) != 16 or not user_cardnumber.isdigit():
        print("The number of digits is not acceptable")
        user_cardnumber = input("Enter your bank account number:")
    user_cardnumber = int(user_cardnumber)
    for user_account in accounts:
        if user_account[0] == user_cardnumber:
            return user_account
    print("Card number not found")
    show_menu()
    return None
show_menu()
choice_input = input("Enter your choice: ")
while not choice_input.isdigit() or int(choice_input) < 0 or int(choice_input) > 6:
    print("Error! Please enter numbers between 0 and 6")
    show_menu()
    choice_input = input("Enter your choice: ")
choice = int(choice_input)
account1=[5894631226873586, 100000, True]
account2=[9876543210123456, 50000, True]
account3=[1234567890123456, 75000, True]
account4=[2222333344445555, 250000, True]
account5=[3333444455556666, 300000, True]
account6=[4444555566667777, 150000, True]
account7=[5555666677778888, 120000, True]
account8=[6666777788889999, 90000, True]
accounts=[account1, account2, account3, account4, account5, account6, account7, account8]
if choice==1:
    name=str(input("Enter your name:"))
    familyname=str(input("Enter your family name:"))
    gender=input("Enter your gender:")
    age=int(input("Enter your age:"))
    while age<0:
        print("The age is not correct, be careful")
        age=int(input("Enter your age:"))
    while gender!="woman" and gender!="man":
        print("Erorr!/ try again")
        gender=input("Enter your gender:")
    balance=0
    card_number=random.randint(1000000000000000,9999999999999999)
    print("Account number for you",card_number)
    user_list={
        "Name": name,
        "Family name": familyname,
        "Gender": gender,
        "Age": age,
        "Bank card number": card_number,
        "Balance": balance,
        "Active": True
    }
    accounts.append([card_number, balance, True])
if choice==2:
    user_account=find_account(accounts)
    if user_account:
        if user_account[2]==True:
            amount=int(input("Enter the deposit amount"))
            while amount<=0:
                print("The amount must be positive")
                amount=int(input("Enter the deposit amount"))
            balance_now=user_account[1]
            balance_new=balance_now+amount
            user_account[1]=balance_new
            print("The deposit was successful")
            print("Previous inventory:",balance_now)
            print("New inventory:",balance_new)
        else:
            print("This account is inactive")
if choice==3:
    user_account = find_account(accounts)
    if user_account:
        if user_account[2]==True:
            amount=int(input("Enter the withdrawal amount"))
            while amount<=0:
                print("The amount must be positive")
                amount=int(input("Enter the withdrawal amount"))
            balance_now=user_account[1]
            if amount>balance_now:
                print("There is not enough inventory")
            else:
                balance_new=balance_now-amount
                user_account[1]=balance_new
                print("The harvest was successful")
                print("Your new inventory:",balance_new)
        else:
            print("This account is inactive")
if choice==4:
    user_account = find_account(accounts)
    if user_account:
        if user_account[2]==True:
            confirm=input("Are you closing your account?")
            if confirm=="yes":
                user_account[2]=False
                print("The account was closed successfully")
            else:
                print("Account closure operation canceled")
        else:
            print("This account has already been deactivated")
    show_menu()
if choice==5:
    user_account = find_account(accounts)
    if user_account:
        if user_account[2]==True:
            print("Your account information:")
            print("Card number:",user_account[0])
            print("Inventory:",user_account[1])
            print("Status: Active")
        else:
            print("This account is inactive")
    show_menu()
if choice==6:
    for i in range(len(accounts)):
        for j in range(i+1, len(accounts)):
            if accounts[i][1] < accounts[j][1]:
                accounts[i],accounts[j]=accounts[j],accounts[i]
    print("Five accounts with the highest balance:")
    for i in range(5):
        print("Card number:",accounts[i][0],"| Inventory:",accounts[i][1])
if choice==0:
    print("goodbye!")
    exit()
