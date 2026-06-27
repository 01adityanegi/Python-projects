balance = 0.0
ATM_PIN = "0001"  
entered_pin = input("Enter your ATM PIN: ")

if entered_pin == ATM_PIN:

    while True:
        print("\n===== ATM Menu =====")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                balance += amount
                print("Deposit successful.")

        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be positive.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print("Withdrawal successful.")

        elif choice == 3:
            print("Current Balance:", balance)

        elif choice == 4:
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid choice. Try again.")

else:
    print("Wrong PIN. Access denied.")
