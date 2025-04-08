# Evan - Savings Goal Tracker
from account_handling import *
from cecilys_helpers import debug

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
 #whichever savings goal you want :)
account=load(name)

#fetching all the goals and amounts




#Savings Goal Tracker Function:
def savingsGoalTracker(budget,account):
    #money=account['total_funds'][-1]
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
            savingsGoalTracker(budget, account)

    #Inner function to check if a variable is a float, and, if so, make it a float, ensuring there are only two decimal places:
    def isFloat(var):
        try:
            var = float(var)
            return var
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingsGoalTracker(budget, account)

        if round(var, 2) != var:
            print("\nToo many decimal places!\n\nPlease try again.")
            savingsGoalTracker(budget, account)

    #Make sure that the user input a valid option:
    whichOne = isInt(whichOne)
    if whichOne == 1:
        pass
    elif whichOne == 2:
        pass
    else:
        print("\nThat's not an option!\n\nPlease try again.")
        savingsGoalTracker(budget, account)

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

        #this is basically just having the user choose what savings goal they want
        savingsGoals=[]
        for x in account['saving goals']:
            if savingsGoals != '':
                savingsGoals.append(x)
        savingAmounts=[]
        for x in account['saving goal amount']:
            if savingsGoals != '':
                savingAmounts.append(x)

        #have the user choose a savings goal to set
        for x in savingsGoals:
            print(x)
            print(f"{savingsGoals.index(x)}. {x} ({savingAmounts[savingsGoals.index(x)]})")
        x=int(input(''))

        item =  savingsGoals[x]
        cost =  savingAmounts[x]

        savingsGoal={
            "Item": item,
            "Cost": cost
        }

        #Show the user how much money is in their savings compared to how much their savings goal cost:
        #print(f"You have ${budget["Savings"]} in your savings, and you need ${savingsGoal["Cost"]} to buy your {savingsGoal["Item"]}.")
        print(f"You have $x in your savings, and you need $x to buy your x.")

#for testing
while True:
    savingsGoalTracker(budget,account)