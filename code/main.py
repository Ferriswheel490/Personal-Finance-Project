# Cecily/Evan/Hasan/Jackson - Main File
from budgeting import budgeting
from currency_conversion import main as currency_convert
from income_expense_handling import income_expense
#from savings_goal_tracker import savings_tracker
from advanced_visuals import *
from essentials import * # Imports cs() (clear screen), int_input() (for integer inputs error handling), end(message) ends the program wiht a message
from account_handling import save
from cecilys_helpers import debug
from savings_goal_tracker import savingsGoalTracker

import csv
import os
import matplotlib.pyplot as plt
import numpy as np

# This is a variable needed for the budgeting function:
budget = {
    "Rent": 0,
    "Food": 0,
    "Gas": 0,
    "Spending": 0,
    "Saving": 0
}


# I moved the password handling to the account handling file -Cecily


def main(): # Main function that runs the UI
    account=sign_in()
    if account == False: end("Bye bye!")

def main(savingsGoal): # Main function that runs the UI
    account = sign_in()
    if account==False: return

    while True:
        cs() # Clears the screen (cleaner UI)
        choice = int_input("""
Financial Manager

1. Currency conversion
2. Budgeting
3. Income and expenses handling
4. Saving goal tracker
5. Show pie chart
6. Exit
                           
Choose option (1-6): """) # Choice of what they want to do

        if choice == 1: # Currency conversion

        if choice == 1: # Currency conversion
            currency_convert()
        elif choice == 2: # Budgeting
            budgeting(0)
        elif choice == 3: # Income and expense handling
            income_expense(account)
        elif choice == 4: # saving goal tracker
            savingsGoalTracker(account, savingsGoal)
        elif choice == 5: # pie chart
            pie([16, 16, 16, 16, 16, 20],['A', 'B', 'C', 'D', 'E','F'],['red', 'orange', 'yellow', 'green', 'blue','purple'],"Test Title")
        elif choice == 6: # Exits/Ends program
            end("Bye bye!") # 
        elif choice == 4: # If they pick choice 4
            print("sorry Evan hasn't done that part of his code yet come back when he is done")
            return main()

        elif choice == 5: # If they pick choice 5

            pie([16, 16, 16, 16, 16, 20],['A', 'B', 'C', 'D', 'E','F'],['red', 'orange', 'yellow', 'green', 'blue','purple'],"Test Title")
        elif choice == 6: # exit
            end("Bye bye!") # Exits/Ends program

        else:
            input("Invalid Input! (Choost an integer from 1 to 6)\nPress enter to continue") # Error handling



#debug()
main()