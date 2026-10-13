# Q10. ATM Withdrawal Simulator using while:
# Start with a balance of Rs. 10,000.
# Continuously show the user options to check balance, deposit money, withdraw money, or exit.
# The program should continue until the user explicitly chooses Exit.

START_BALANCE = 10000

def atm_simulator(balance:float):
    while True:
        print()
        print("===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        try:
            choice = input("\nEnter your choice (1-4): ")

            if choice == "1":
                print("\nCurrent balance: Rs.", balance)

            elif choice == "2":
                amount = float(input("\nEnter amount to deposit: "))
                if amount <= 0:
                    print("\nDeposit amount must be greater than 0.")
                else:
                    balance += amount
                    print("\nDeposited Rs.", amount, "| New balance: Rs.", balance)

            elif choice == "3":
                amount = float(input("\nEnter amount to withdraw: "))
                if amount <= 0:
                    print("\nWithdrawal amount must be greater than 0.")
                elif amount > balance:
                    print("\nInsufficient balance. Available: Rs.", balance)
                else:
                    balance -= amount
                    print("\nWithdrew Rs.", amount, "| New balance: Rs.", balance)

            elif choice == "4":
                print("\nThank you for using the ATM. Goodbye!")
                break

            else:
                print("\nInvalid choice. Please enter a number from 1 to 4.")
        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")
        except KeyboardInterrupt:
             print(f"\nUser interrupted the input. Exiting the program.")


if __name__ == "__main__":
    atm_simulator(START_BALANCE)