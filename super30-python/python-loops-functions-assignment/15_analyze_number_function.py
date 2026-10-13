# Q15. Reusable Number Analysis Function:
# Create def analyze_number(number).
# It should determine whether the number is positive/negative/zero, even/odd, and prime/not prime.
# Return the results rather than only printing them.


def is_prime(number):
    if number < 2:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def analyze_number(number):
    if number > 0:
        sign = "Positive"
    elif number < 0:
        sign = "Negative"
    else:
        sign = "Zero"

    parity = "Even" if number % 2 == 0 else "Odd"
    prime = "Prime" if is_prime(number) else "Not Prime"

    return sign, parity, prime


if __name__ == "__main__":
    while True:
        try:
            number = int(input("Enter a whole number : "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            raise SystemExit

    sign, parity, prime = analyze_number(number)
    print(f"\nNumber : {number}")
    print(f"Sign   : {sign}")
    print(f"Parity : {parity}")
    print(f"Prime  : {prime}")
