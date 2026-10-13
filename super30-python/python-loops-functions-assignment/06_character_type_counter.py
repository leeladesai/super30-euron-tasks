# Q6. Vowel, Consonant, Digit and Space Counter: 
# Create a program that analyzes a sentence and 
# counts vowels, consonants, digits, spaces, and special characters separately.


def capture_user_input() -> str:
    '''Function to capture user input'''
    while True:
        try:
            user_input = input(str("Enter a sentence: "))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a valid string.")
            continue
        except KeyboardInterrupt:
            print("\nUser interrupted the input. Exiting the program.")
            exit(0)

def character_type_counter(input_string: str) -> dict:
    '''Function to count vowels, consonants, digits, spaces, and special characters in a string'''
    counts = {
        'vowels': 0,
        'consonants': 0,
        'digits': 0,
        'spaces': 0,
        'special_characters': 0
    }
    
    for char in input_string:
        if char.isalpha():
            if char.lower() in 'aeiou':
                counts['vowels'] += 1
            else:
                counts['consonants'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        else:
            counts['special_characters'] += 1
            
    return counts

if __name__ == "__main__":
    user_input = capture_user_input()
    counts = character_type_counter(user_input)
    
    print("\nCharacter Type Counts:")
    for category, count in counts.items():
        print(f"{category.capitalize()}: {count}")
        