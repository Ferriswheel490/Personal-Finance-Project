# Cecily/Evan/Hasan/Jackson - Main File

from essentials import * # Imports cs() (clear screen), int_input() (for integer inputs error handling), end(message) ends the program wiht a message
import os
def sign_in(username, password, user_database, account, make_account):
    account =  input("do you have an account (y/n): ")
    if account == "yes":
        username_input = input("Username: ")
        password_input = input("Password: ")
        result = sign_in(username_input, password_input)
        print(result)
    elif account == "no":
        make_account = input("do you wanna make an account (y/n): ")
        if make_account == "no":
            return sign_in()
        elif make_account == "yes":
            username_input = input("Username: ")
            password_input = input("Password: ")    

# We need a function that takes username and password and either makes a new account with a setup process or loads the old account into a master list -Jackson

def main(): # Main function that runs the UI
    while True:
        cs() # Clears the screen (cleaner UI)
        choice = int_input("""
Financial Manager

1. Option Here
2. Option Here
3. Option Here
4. Option Here
5. Exit
                           
Choose option (1-5): """) # Choice of what they want to do
        if choice == 1: # If they pick choice 1
            pass
        elif choice == 2: # If they pick choice 2
            pass
        elif choice == 3: # If they pick choice 3
            pass
        elif choice == 4: # If they pick choice 4
            pass
        elif choice == 5: # If they pick choice 5
            end("Bye bye!") # Exits/Ends program
        else:
            input("Invalid Input! (Choost an integer from 1 to 5)\nPress enter to continue") # Error handling

