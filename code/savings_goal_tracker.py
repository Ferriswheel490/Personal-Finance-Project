# Evan - Savings Goal Tracker
from account_handling import save,load
from cecilys_helpers import debug
from essentials import int_input
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


#fetching all the goals and amounts




#Savings Goal Tracker Function:
def savingsGoalTracker(account):
    #money=account['total_funds'][-1]
    update={'name':'','date':'','total_funds':'','expense_source':'','expense_amount':'','income_source':'','income_amount':'', 'budget_limits':'', 'budget_limit_amount':'','rent':'','food':'','gas':'','saving':'','spending':''}
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
            savingsGoalTracker(account)

    #Inner function to check if a variable is a float, and, if so, make it a float, ensuring there are only two decimal places:
    def isFloat(var):
        try:
            var = float(var)
            return var
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            savingsGoalTracker(account)

        if round(var, 3) != var:
            print("\nToo many decimal places!\n\nPlease try again.")
            savingsGoalTracker(account)

    #Make sure that the user input a valid option:
    whichOne = isInt(whichOne)
    if whichOne == 1:
        pass
    elif whichOne == 2:
        pass
    else:
        print("\nThat's not an option!\n\nPlease try again.")
        savingsGoalTracker(account)

    #If they want to set a savings goal:
    if whichOne == 1:

        #Tell the user that their new savings goal will override any old ones:
        #print("\nYour new savings goal will override any old ones.")

        #Ask the user what item they want to save up for:
        savingsGoalItem = input("\nWhat is the item you want to save up for?\n")

        #Ask the user how much the item they want to save up for costs:
        savingsGoalCost = input("\nHow much does that thing cost? (number value, up to two decimals)\n")
        

        #Set the user’s new saving goal in the saving goal dictionary:
        savingsGoalCost=isFloat(savingsGoalCost)

        update['saving goals']= savingsGoalItem
        update['saving goal amount']= savingsGoalCost
        print(account['name'])
        save(account['name'][0],update)
        return

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
            if len(x)>0:
                #print(x)
                print(f"{savingsGoals.index(x)}. {x} ({savingAmounts[savingsGoals.index(x)]})")
        f=isInt(input(''))

        item =  savingsGoals[f]
        cost =  savingAmounts[f]
        money=[]
        for x in account['total_funds']:
            if x != '':money.append(x)
        print(f"You have ${money[-1]} in your savings, and you need ${cost} to buy your {item}.")
        return
