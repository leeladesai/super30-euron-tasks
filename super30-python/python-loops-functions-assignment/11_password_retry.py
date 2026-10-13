# Q11. Password Retry System: 
# Store a predefined password and give the user a maximum of three attempts to enter it correctly. 
# Use a while loop. After three incorrect attempts, display "Account Locked".

from pwinput import pwinput


USER_PASSWORD = "password@123"
MAX_ATTEMPTS = 3

def pwd_checker() -> bool:
    attempts=0
    try:
        while attempts < MAX_ATTEMPTS:
            attempts+=1
            pwd = pwinput("\nEnter the user password : ")
            if pwd == USER_PASSWORD:
                print("\n Login sucess!!!")
                return True
            else:
                remaining = MAX_ATTEMPTS-attempts
                if remaining > 0:
                    print(f"\nEntered password is incorrect. Please try again!! {remaining} attmept(s) left")
        print("\nAccount Locked!!!")
        return False
    except KeyboardInterrupt:
        print(f"\nUser interrupted the input. Exiting the program.")
        exit(0)


if __name__ == "__main__":
    pwd_checker()