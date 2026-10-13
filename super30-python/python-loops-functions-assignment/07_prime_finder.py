# Q7. Prime Number Finder: Ask the user for a starting and ending number.
# Print all prime numbers within that range using nested loops.

def capture_user_input() -> tuple:
    '''Function to capture user input for starting and ending numbers'''
    while True:
        try:
            start_num = int(input("Enter the starting number: "))
            end_num = int(input("Enter the ending number: "))
            if start_num > end_num:
                print("Starting number should be less than or equal to ending number. Please try again.")
                continue
            return start_num, end_num
        except ValueError:
            print("Invalid input. Please enter valid integers.")
            continue
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            exit(0)

def is_prime(num: int) -> bool:
    '''Function to check if a number is prime'''
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    start, end = capture_user_input()
    print(f"\nPrime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")