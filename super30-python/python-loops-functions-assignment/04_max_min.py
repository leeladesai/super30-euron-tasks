# Q4. Find Maximum and Minimum Without max() / min(): 
# Write a program that finds the largest and smallest values in a list using loops only.


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

def min_max(numbers):
    '''Function to find minimum and maximum values in a list of numbers'''
    
    if not numbers:
        print("The list is empty. Cannot determine min and max values.")
        return None, None
    
    min_value = numbers[0]
    max_value = numbers[0]
    
    for num in numbers:
        if num < min_value:
            min_value = num
        if num > max_value:
            max_value = num
    
    print(f"\nMinimum value: {min_value}")
    print(f"Maximum value: {max_value}\n")
    
    return min_value, max_value

if __name__ == "__main__":
    numbers = capture_numbers(max_numbers=10)
    min_max(numbers)