# Cecily/Evan/Fairus/Jackson - Main File
from cecilys_helpers import debug
from budgeting import budgeting
from currency_conversion import convert as currency_convert
from income_expense_handling import income_expense
#from savings_goal_tracker import savings_tracker
from advanced_visuals import *
from essentials import * # Imports cs() (clear screen), int_input() (for integer inputs error handling), end(message) ends the program wiht a message
from account_handling import *

from account_handling import save, sign_in
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

    



def main(): # Main function that runs the UI
    account=load('test')#sign_in()
    
   
    def options():
        cs() # Clears the screen (cleaner UI)
        choice = int_input("""
Financial Manager

1. Currency conversion
2. Budgeting
3. Income and expenses handling
4. Saving goal tracker
5. Show budget pie chart
6. Exit
                        
Choose option (1-6): """) # Choice of what they want to do
        if choice == 1: # Currency conversion
            print(currency_convert()) #cecily
            options()
        elif choice == 2: # Budgeting
            budgeting(account)
            options()
        elif choice == 3: # Income and expense handling
            income_expense(account)
            options()
        elif choice == 4: # Savings goal tracker
            savingsGoalTracker(account)
            options()
        elif choice == 5: # Show budget pie chart
            def latest(parameter):
                num=0
                
                for x in account[parameter]:
                    
                    if x != '':
                        num=x
                return num
            def budget(parameter):
                return float(latest(parameter))*100/float(latest('total_funds'))
            numbers=[budget('rent'), budget("food"), budget("gas"), budget("spending"), budget("saving")]
            broken=True
            for x in numbers:
                if x != 0.0:
                    broken=False
            if broken == False:
                pie(numbers,['Rent', 'Food', 'Gas', 'Spending', 'Saving'],['red', 'yellow', 'green', 'blue','purple'],"Budget Pie Chart")
            else: print("you do not have any budget to graph")
            options()
        elif choice == 6: # If they pick choice 6
            end("Bye bye!") # Exits/Ends program
        else:
            input("Invalid Input! (Choost an integer from 1 to 6)\nPress enter to continue") # Error handling
            options()

    options()



#debug()
'''purge()
new_acc('test','password')'''
main() 