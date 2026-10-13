# Q8. Pattern Generator: 
# Using nested for loops, generate the pattern (1 / 1 2 / 1 2 3 / 1 2 3 4 / 1 2 3 4 5, one row per line) 
# for a user-supplied value of N.

def pattern_generator(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  # Move to the next line after each row

def capture_user_input():
    while True:
        try:
            n = int(input("Enter a positive integer N for the pattern: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            return n
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting gracefully.")
            exit()

if __name__ == "__main__":
    n = capture_user_input()
    pattern_generator(n)