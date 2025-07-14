# Simple ATM Simulation using exception handling

# Initial balance
balance = 1000.0

def display_menu():
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

while True:
    try:
        display_menu()
        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == 2:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            balance += amount
            print(f"${amount:.2f} deposited successfully. New balance: ${balance:.2f}")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > balance:
                raise ValueError("Insufficient balance.")
            balance -= amount
            print(f"${amount:.2f} withdrawn successfully. New balance: ${balance:.2f}")

        elif choice == 4:
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)
