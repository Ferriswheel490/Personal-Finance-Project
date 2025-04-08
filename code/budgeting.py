# Evan - Budgeting

# from advanced_visuals import *
# JACKSON FIX THIS LATER ^
from account_handling import load
#TEMPORARY FOR TES iTING:
budget = {
    "Rent": 0,
    "Food": 0,
    "Gas": 0,
    "Spending": 0,
    "Saving": 0
}

#Budgeting Function:
def budgeting(account, budget):
    money=account['total_funds']
    #Inner function to check if a variable is an integer, and, if so, make it an integer:
    def isInt(var):
        try:
            var = int(var)
            return var
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            budgeting(money, budget)

    #Inner function to check if a variable is a float, and, if so, make it a float, ensuring there are only two decimal places:
    def isFloat(var):
        try:
            var = float(var)
            return var
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            budgeting(money, budget)

        if round(var, 2) != var:
            print("\nToo many decimal places!\n\nPlease try again.")
            budgeting(money, budget)

    #Ask the user if they want to set budget limits or compare expenses to budget:
    budgetChoice = input("\nWould you like to set budget limits or compare an expense to your budget?\n1. new budget\n2. compare expense to budget\n3. exit\n")

    #Make sure that the user input a valid option:
    budgetChoice = isInt(budgetChoice)
    if budgetChoice == 1 or budgetChoice == 2 or budgetChoice == 3:
        pass
    else:
        print("\nThat's not an option!\n\nPlease try again.")
        budgeting(money, budget)

    #If the user chose to set budget limits:
    if budgetChoice == 1:

        #Tell the user what the budgeting categories are(Rent, Food, Gas, Spending, Saving):
        print("\nThe categories are as follows:\nRent, Food, Gas, Spending, Saving")

        #Tell the user how much total money they have to allocate:
        print("\nYou have $" + str(float(money)) + " to allocate.")

        #Ask the user how much money they want to allocate to their rent budget:
        newRentBudget = input("\nHow much money would you like to allocate to your rent budget?\n$")
        newRentBudget = isFloat(newRentBudget)

        #Ask the user how much money they want to allocate to their food budget:
        newFoodBudget = input("\nHow much money would you like to allocate to your rent budget?\n$")
        newFoodBudget = isFloat(newFoodBudget)

        #Ask the user how much money they want to allocate to their gas budget:
        newGasBudget = input("\nHow much money would you like to allocate to your rent budget?\n$")
        newGasBudget = isFloat(newGasBudget)

        #Ask the user how much money they want to allocate to their spending budget:
        newSpendingBudget = input("\nHow much money would you like to allocate to your rent budget?\n$")
        newSpendingBudget = isFloat(newSpendingBudget)

        #Ask the user how much money they want to allocate to their saving budget:
        newSavingBudget = input("\nHow much money would you like to allocate to your saving budget?\n$")
        newSavingBudget = isFloat(newSavingBudget)

        #If the user’s percentages/number amounts DO NOT add up to 100% of the user’s total money:
        totalBudget = newRentBudget + newFoodBudget + newGasBudget + newSpendingBudget + newSavingBudget
        if totalBudget != money:

            #Tell the user that their numbers don’t add up and they need to try again:
            print("\nThose numbers don't add up to your total money!\n\nPlease try again.")

            #Run the budgeting function to keep the program running:
            budgeting(money, budget)

        #If the user’s percentages/number amounts DO add up to 100% of the user’s total money:
        else:

            #Set the user’s new budget in a variable:
            budget = {
                "Rent": newRentBudget,
                "Food": newFoodBudget,
                "Gas": newGasBudget,
                "Spending": newSpendingBudget,
                "Saving": newSavingBudget
            }

            #Tell the user that the process was successful:
            print("\nYour new budget has been set!")

    #If the user chose to compare expenses to budget:
    if budgetChoice == 2:

        #Ask the user what their expense is:
        expenseThing = input("\nWhat thing are you aiming to buy?\n")

        #Ask the user how much their expense costs:
        expenseCost = input("\nHow much does it cost?\n$")
        expenseCost = isFloat(expenseCost)

        #Ask the user what budget category it applies to:
        category = input("\nWhat budget category does your expense apply to? (Please type exactly)\nRent\nFood\nGas\nSpending\nSaving\n")

        #Make sure the user chose a valid option:
        validOption = False
        if category == "Rent":
            validOption = True
        if category == "Food":
            validOption = True
        if category == "Gas":
            validOption = True
        if category == "Spending":
            validOption = True
        if category == "Saving":
            validOption = True
        if validOption == False:
            print("\nYou either made a spelling mistake, or did not choose a valid option.\n\nPlease try again.")
            budgeting(money, budget)

        #If the user DOES NOT have enough money in their budget for the expense:
        if expenseCost > budget[category]:

            #Tell the user that they do not have enough money, and show them how much more money they still need:
            moneyStillNeeded = expenseCost - budget[category]
            print(f"\nYou do not have enough money to purchase the {expenseThing}.\nYou still need an additional ${moneyStillNeeded}.")

        #If the user DOES have enough money in their budget for the expense:
        else:

            #Tell the user that they have enough money, and show them how much they exceeded their expense by:
            moneyExceeded = budget[category] - expenseCost
            print(f"You have enough money to purchase the {expenseThing}!\nYou exceeded the amount needed to pay the expense by ${moneyExceeded}.")

    #If the user chose to exit:
    if budgetChoice == 3:

        #Exit this function and return to the main page:
        pass

<<<<<<< HEAD
    #TEMP FOR TESTING:
    budgeting(money, budget)

budgeting(load('test'), budget)
=======
budgeting(3000, budget)
>>>>>>> 2319747ecc5585b1d1394388dbffc37198ed80e6
