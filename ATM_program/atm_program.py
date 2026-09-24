balance = 50000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Your current balance is:", balance)

    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit successful. New balance:", balance)

    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance!")
        else:
            balance = balance - amount
            print("Withdrawal successful. New balance:", balance)

    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1-4.")