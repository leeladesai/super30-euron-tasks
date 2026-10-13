# Q19. Bank Account Mini Application:
# Create functions for deposit(), withdraw(), check_balance(), and transaction_history().
# Use a while loop to keep the banking application running.
# Prevent withdrawals when sufficient balance is unavailable.

# account structure: {"balance": float, "history": [(type, amount, balance_after), ...]}


def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be greater than 0.")
        return False
    account["balance"] += amount
    account["history"].append(("Deposit", amount, account["balance"]))
    print(f"Deposited Rs. {amount:.2f}")
    return True


def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than 0.")
        return False
    if amount > account["balance"]:
        print(f"Insufficient balance. Available: Rs. {account['balance']:.2f}")
        return False
    account["balance"] -= amount
    account["history"].append(("Withdraw", amount, account["balance"]))
    print(f"Withdrew Rs. {amount:.2f}")
    return True


def check_balance(account):
    print(f"Current balance: Rs. {account['balance']:.2f}")


def transaction_history(account):
    if not account["history"]:
        print("No transactions yet.")
        return
    print(f"\n{'#':<4}{'Type':<10}{'Amount':>12}{'Balance':>14}")
    print("-" * 40)
    for i, (kind, amount, balance_after) in enumerate(account["history"], start=1):
        print(f"{i:<4}{kind:<10}{amount:>12.2f}{balance_after:>14.2f}")


def read_amount(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None


def bank_app():
    account = {"balance": 0.0, "history": []}
    while True:
        print()
        print("===== Bank Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        try:
            choice = input("\nEnter your choice (1-5): ")

            if choice == "1":
                amount = read_amount("Enter amount to deposit : ")
                if amount is not None:
                    deposit(account, amount)
            elif choice == "2":
                amount = read_amount("Enter amount to withdraw : ")
                if amount is not None:
                    withdraw(account, amount)
            elif choice == "3":
                check_balance(account)
            elif choice == "4":
                transaction_history(account)
            elif choice == "5":
                print("Thank you for banking with us. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            break


if __name__ == "__main__":
    bank_app()
