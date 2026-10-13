# Q13. Menu-Driven Calculator:
# Build a continuously running calculator using while.
# Provide Addition, Subtraction, Multiplication, Division, Modulus, and Exit operations.
# Handle division by zero properly.


def calculator():
    while True:
        print()
        print("===== Calculator Menu =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exit")

        try:
            choice = input("\nEnter your choice (1-6): ")

            if choice == "6":
                print("\nThank you for using the calculator. Goodbye!")
                break

            if choice not in ("1", "2", "3", "4", "5"):
                print("\nInvalid choice. Please enter a number from 1 to 6.")
                continue

            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))

            if choice == "1":
                print(f"\n{num1} + {num2} = {num1 + num2}")
            elif choice == "2":
                print(f"\n{num1} - {num2} = {num1 - num2}")
            elif choice == "3":
                print(f"\n{num1} * {num2} = {num1 * num2}")
            elif choice == "4":
                if num2 == 0:
                    print("\nError: Division by zero is not allowed.")
                else:
                    print(f"\n{num1} / {num2} = {num1 / num2}")
            elif choice == "5":
                if num2 == 0:
                    print("\nError: Modulus by zero is not allowed.")
                else:
                    print(f"\n{num1} % {num2} = {num1 % num2}")
        except ValueError:
            print("\nInvalid input. Please enter numeric values.")
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            break


if __name__ == "__main__":
    calculator()
