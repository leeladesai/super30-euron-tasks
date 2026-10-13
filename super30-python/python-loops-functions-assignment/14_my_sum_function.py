# Q14. Create Your Own sum() Function:
# Write def my_sum(numbers).
# It should accept a list of numbers and return their sum without using Python's built-in sum().


def my_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def read_numbers():
    while True:
        try:
            text = input("Enter numbers separated by spaces : ")
            return [float(item) for item in text.split()]
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")


if __name__ == "__main__":
    try:
        numbers = read_numbers()
        print(f"Numbers : {numbers}")
        print(f"Sum     : {my_sum(numbers)}")
    except KeyboardInterrupt:
        print("\nUser interrupted the input. Exiting the program.")
