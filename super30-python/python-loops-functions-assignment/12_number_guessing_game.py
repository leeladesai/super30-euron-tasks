# Q12. Number Guessing Game: 
# Generate a random number between 1-100. 
# Keep asking the user to guess until they find the correct number. 
# After each incorrect guess, display "Too High" or "Too Low". 
# Finally display the number of attempts taken.

import random

def num_guessing_game():

    attempts = 0
    chosen_num = random.randint(1,100)

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100. Can you guess it?")

    while True:
        try:
            attempts+=1
            user_input_num = int(input("Guess the Number : "))

            if user_input_num == chosen_num:
                print(f"You Won in {attempts} attempt(s)!!!! the chossen number is {chosen_num}")
                break
            elif user_input_num > chosen_num:
                print("\n You guess is Too High!!!")
            else:
                print("\n You guess is Too Low!!!")
        except ValueError:
            print("Invalid input. Please enter a valid string.")
            continue
        except KeyboardInterrupt:
            print(f"\nUser interrupted the input. Exiting the program.")
            exit(0)
        
if __name__ == "__main__":
    num_guessing_game()
