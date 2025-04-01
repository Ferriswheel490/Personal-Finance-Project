# Cecily/Evan/Hasan/Jackson - Main File
from budgeting import budgeting
from currency_conversion import currency_convert
from income_expense_handling import income_expense
from savings_goal_tracker import goal_tracker

from essentials import * # Imports cs() (clear screen), int_input() (for integer inputs error handling), end(message) ends the program wiht a message
import csv
import os

USER_FILE = "user.csv"

# Check if CSV file exists, create it if not
def initialize_file():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Header row

# Load users from CSV into a dictionary
def load_users():
    users = {}
    with open(USER_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) == 2:  # Ensure valid data
                users[row[0]] = row[1]
    return users

# Save a new user to the CSV file
def save_user(username, password):
    with open(USER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

# Sign-in function
def sign_in():
    initialize_file()
    users = load_users()
    
    has_account = input("Do you have an account? (yes/no): ").strip().lower()
    
    if has_account == "no":
        create = input("Do you want to create one? (yes/no): ").strip().lower()
        if create == "yes":
            return create_account(users)
        else:
            print("Okay, exiting...")
            return

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful! Welcome back,", username)
    else:
        print("Invalid username or password.")

# Account creation function
def create_account(users):
    username = input("Choose a username: ")
    
    if username in users:
        print("Username already taken. Try again.")
        return create_account(users)
    
    password = input("Choose a password: ")
    save_user(username, password)
    print("Account created successfully!")

# Run the sign-in function
sign_in()
 

# We need a function that takes username and password and either makes a new account with a setup process or loads the old account into a master list -Jackson

def main(): # Main function that runs the UI
    while True:
        cs() # Clears the screen (cleaner UI)
        choice = int_input("""
Financial Manager

1. currency cnversion
2. budgeting
3. income and expenses handling
4. saving goal tracker
5. show pie chart
6. Exit
                           
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
            pass
        elif choice == 6: # If they pick choice 6
            end("Bye bye!") # Exits/Ends program
        else:
            input("Invalid Input! (Choost an integer from 1 to 5)\nPress enter to continue") # Error handling

main()