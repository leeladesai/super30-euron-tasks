# Q2. Multiplication Table Generator
# Take a number from the user and print its multiplication table from 1 × N through 10 × N using a for loop. Then modify the program so the ending range can also be


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
    

def multiplication_table(num: int):
    '''Function to generate multiplication table for a given number'''
    min = 1
    max = 10
    
    print(f"\nMultiplication Table for {num}:\n")
    
    for i in range(1, max + 1):
        print(f"{i} x {num} = {num * i}")
    print(f"\n--------Multiplication Table for {num} from 1 to {max} generated successfully.---------\n")


if __name__ == "__main__":
    min = 1
    max = 10

    num = fetch_user_input(min, max)
    multiplication_table(num)
