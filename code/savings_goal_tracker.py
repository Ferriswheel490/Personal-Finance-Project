# Evan - Savings Goal Tracker
from account_handling import *

#TEMPORARY FOR TESTING:
budget = {
    "Rent": 0,
    "Food": 0,
    "Gas": 0,
    "Spending": 0,
    "Saving": 0
}

#TEMPORARY FOR TESTING:
savingsGoal = {
    "Item": "Not set yet.",
    "Cost": 0
}

name='evan' #evan make an account and then have the name here pretty please <3
x=0 #whichever savings goal you want :)
account=export(name)
item =  account['saving goals'][x]
cost =  account['saving goal amount'][x]

savingsGoal={
    "Item": item,
    "Cost": cost
}

#Savings Goal Tracker Function:
def savingsGoalTracker(account, savingsGoal):
    money=account['total_funds'][-1]
    change={'name':'','date':'','total_funds':'','expense_source':'','expense_amount':'','income_source':'','income_amount':'','saving goals':'', 'saving goal amount':'', 'budget_limits':'', 'budget_limit_amount':''}
    #you are only using 'saving goals':'', 'saving goal amount':''

    #Ask the user if they want to set a savings goal or check their progress towards the goal:
    whichOne = input("\nWould you like to set a savings goal or check your progress towards your savings goal?\n1. Set a Savings Goal\n2. Check Progress Towards Savings Goal\n")

    #Inner function to check if a variable is an integer, and, if so, make it an integer:
    def isInt(var):
        try:
            var = int(var)
            return var
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingsGoalTracker(budget, savingsGoal)

    #Inner function to check if a variable is a float, and, if so, make it a float, ensuring there are only two decimal places:
    def isFloat(var):
        try:
            var = float(var)
            return var
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingsGoalTracker(budget, savingsGoal)

        if round(var, 2) != var:
            print("\nToo many decimal places!\n\nPlease try again.")
            savingsGoalTracker(budget, savingsGoal)

    #Make sure that the user input a valid option:
    whichOne = isInt(whichOne)
    if whichOne == 1:
        pass
    elif whichOne == 2:
        pass
    else:
        print("\nThat's not an option!\n\nPlease try again.")
        savingsGoalTracker(budget, savingsGoal)

    #If they want to set a savings goal:
    if whichOne == 1:

        #Tell the user that their new savings goal will override any old ones:
        print("\nYour new savings goal will override any old ones.")

        #Ask the user what item they want to save up for:
        savingsGoalItem = input("\nWhat is the item you want to save up for?\n")

        #Ask the user how much the item they want to save up for costs:
        savingsGoalCost = input("\nHow much does that thing cost? (number value, up to two decimals)\n")
        isFloat(savingsGoalCost)

        #Set the user’s new saving goal in the saving goal dictionary:
        
        change['saving goals']= savingsGoalItem
        change['saving goal amount']= savingsGoalCost
        
        save(account,change)

    #If they want to check their progress towards their savings goal:
    if whichOne == 2:

        #Make sure the user has set a savings goal already:
        if savingsGoal["Item"] == "Not set yet.":
            print("\nYou have not set a savings goal yet.\n\nPlease try again.")
            savingsGoalTracker(budget, savingsGoal)

        #Show the user how much money is in their savings compared to how much their savings goal cost:
        print(f"You have ${budget["Savings"]} in your savings, and you need ${savingsGoal["Cost"]} to buy your {savingsGoal["Item"]}.")

#for testing
savingsGoalTracker(account, savingsGoal)