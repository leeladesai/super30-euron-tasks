# Q3. Sum and Average Without sum(): Given a list of numbers, calculate the total and average using a loop. Do not use Python's built-in sum() function.


def capture_numbers(max_numbers:int):
    '''Function to capture numbers from user input'''
    while True:
        try:
            capture_number = input(f"Enter numbers separated by spaces (max {max_numbers} numbers): ")
            numbers = list(map(int, capture_number.split()))
            if len(numbers) > max_numbers:
                print(f"You have entered more than {max_numbers} numbers. Only the first {max_numbers} will be considered.")
                numbers = numbers[:max_numbers]
                continue
            return numbers
        except ValueError:
            print("Invalid input. Please enter only integers separated by spaces.")
            continue
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            exit(0)


def sum_and_average(numbers):
    '''Function to calculate sum and average of a list of numbers'''
    
    total = 0
    count = len(numbers)
    
    for num in numbers:
        total += num
    
    average = total / count if count > 0 else 0
    print(f"\nSum of entered numbers: {total}")
    print(f"Average of entered numbers: {average}\n")

if __name__ == "__main__":
    numbers = capture_numbers(max_numbers=10)
    sum_and_average(numbers)