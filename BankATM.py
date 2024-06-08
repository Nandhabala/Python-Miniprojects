def showbalance(balance):
    print("********************")
    print(f"Your balance is Rs:{balance:.2f}")
    print("********************")

def deposit():
    print("********************")
    amount = float(input("Enter the deposit amount: "))
    print("********************")
    if amount < 0:
        print("********************")
        print("This is an invalid amount")
        print("********************")
        return 0
    else:
        return amount

def withdraw(balance):
    print("********************")
    amount = float(input("Enter the withdraw amount: "))
    print("********************")
    if amount > balance:
        print("********************")
        print("Insufficient balance")
        print("********************")
        return 0
    elif amount < 0:
        print("********************")
        print("Amount must be greater than zero")
        print("********************")
        return 0
    else:
        return amount

def main():
    balance = 0
    running = True

    while running:
        print("********************")
        print("Bank Program")
        print("********************")
        print("1. SHOW BALANCE")
        print("2. DEPOSIT")
        print("3. WITHDRAW")
        print("4. EXIT")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            showbalance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            running = False
        else:
            print("This is an invalid choice, please enter a valid choice")
    print("***** Thank you *****")

if __name__ == "__main__":
    main()
