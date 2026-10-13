# Q2. Multiplication Table Generator
# Take a number from the user and print its multiplication table from 1 × N through 10 × N using a for loop. Then modify the program so the ending range can also be entered by the user.

import sys
from typing import Optional

DEFAULT_END = 10
MAX_END = 100


def fetch_user_input(prompt: str, min_val: int, max_val: Optional[int] = None) -> int:
    '''Function to fetch an integer from the user, optionally bounded'''
    while True:
        try:
            input_num = int(input(prompt))
        except ValueError:
            print("\nEntered value is not an integer. Please try again.")
            continue
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            sys.exit(0)

        if validate_input(input_num, min_val, max_val):
            return input_num


def validate_input(input_num: int, min_val: int, max_val: Optional[int] = None) -> bool:
    '''Function to validate user input'''
    if input_num < min_val or (max_val is not None and input_num > max_val):
        if max_val is None:
            print(f"\nEntered number must be at least {min_val}. Please try again.")
        else:
            print(f"\nEntered number is not in the range of {min_val} to {max_val}. Please try again.")
        return False
    return True


def multiplication_table(num: int, end: int = DEFAULT_END):
    '''Function to generate multiplication table for a given number from 1 to end'''
    print(f"\nMultiplication Table for {num}:\n")

    for i in range(1, end + 1):
        print(f"{i} x {num} = {num * i}")
    print(f"\n--------Multiplication Table for {num} from 1 to {end} generated successfully.---------\n")


if __name__ == "__main__":
    num = fetch_user_input("\nEnter a number : ", 1)
    end = fetch_user_input(f"\nEnter the ending range (1 to {MAX_END}, e.g. {DEFAULT_END}) : ", 1, MAX_END)
    multiplication_table(num, end)
