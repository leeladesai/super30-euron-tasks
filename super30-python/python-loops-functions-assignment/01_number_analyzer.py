# Q1. Number Analyzer using for loop: Take a number N from the user. Print all numbers from 1 to N, identify whether each number is even or odd, and finally display the total count of even and odd numbers.

def fetch_user_input(min_val: int, max_val: int):
    '''Function to fetch user input'''
    while True:
        try:
            input_num = int(input(f"\nEnter a number between {min_val} and {max_val} : "))
            if not validate_input(input_num, min_val, max_val):
                continue
            else:
                return input_num
        except ValueError:
            print(f"\nEntered value is not an integer. Please try again.")
            continue
        except KeyboardInterrupt:
            print(f"\nUser interrupted the input. Exiting the program.")
            exit(0)

def validate_input(input_num: int, min_val: int, max_val: int) -> bool:
    '''Function to validate user input'''
    if not (min_val <= input_num <= max_val):
        print(f"\nEntered number is not in the range of {min_val} to {max_val}. Please try again.")
        return False
    else:
        return True

def number_analyzer(num: int):
    '''Function to analyze the number and print even/odd numbers'''

    even_count = 0
    odd_count = 0

    for i in range(1, num + 1):
        if i % 2 == 0:
            print(f"{i} is Even")
            even_count += 1
        else:
            print(f"{i} is Odd")
            odd_count += 1

    print(f"\nTotal Even numbers: {even_count}")
    print(f"Total Odd numbers: {odd_count}\n")


if __name__ == "__main__":
    min = 1
    max = 100
    num = fetch_user_input(min, max)
    print(f"\nAnalyzing numbers from 1 to {num} for even/odd :")
    number_analyzer(num)