# Q5. Character Frequency Counter: 
# Take a string from the user and calculate how many times each character occurs. 
# Example: "banana" should identify the frequencies of b, a, and n.

def capture_user_input() -> str:
    '''Function to capture user input'''
    while True:
        try:
            user_input = input(str("Enter a string: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid string.")
            continue
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            exit(0)

def character_frequency(input_string: str) -> dict:
    '''Function to calculate character frequency in a string'''
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == "__main__":
    user_input = capture_user_input()
    frequency = character_frequency(user_input)
    
    print("\nCharacter Frequencies:")
    for char, count in frequency.items():
        print(f"'{char}': {count}")
