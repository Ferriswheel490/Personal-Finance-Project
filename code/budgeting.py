# Evan - Budgeting

# from advanced_visuals import *
# JACKSON FIX THIS LATER ^
from account_handling import save, load
from essentials import int_input
#Budgeting Function:
def budgeting(account):
    update={'name':'','date':'','total_funds':'','expense_source':'','expense_amount':'','income_source':'','income_amount':'', 'budget_limits':'', 'budget_limit_amount':'','rent':'','food':'','gas':'','saving':'','spending':''}
    money=0
    for x in account['total_funds']:
        if x != '':
            money = x
    print(money)

   
    money = float(money)
    #Inner function to check if a variable is an integer, and, if so, make it an integer:
    def isInt(var):
        try:
            var = int(var)
            return var
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            budgeting(account)

    #Inner function to check if a variable is a float, and, if so, make it a float, ensuring there are only two decimal places:
    def isFloat(var):
        try:
            var = float(var)
            
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            budgeting(account)

        if round(var, 3) != var:
            print("\nToo many decimal places!\n\nPlease try again.")
            budgeting(account)
        else:
            return var
    #Ask the user if they want to set budget limits or compare expenses to budget:
    budgetChoice = input("\nWould you like to set budget limits or compare an expense to your budget?\n1. new budget\n2. compare expense to budget\n3. exit\n")

    #Make sure that the user input a valid option:
    budgetChoice = isInt(budgetChoice)
    if budgetChoice == 1 or budgetChoice == 2 or budgetChoice == 3:
        pass
    else:
        print("\nThat's not an option!\n\nPlease try again.")
        budgeting(account)

    #If the user chose to set budget limits:
    if budgetChoice == 1:

        #Tell the user what the budgeting categories are(Rent, Food, Gas, Spending, Saving):
        print("\nThe categories are as follows:\nRent, Food, Gas, Spending, Saving")

        #Tell the user how much total money they have to allocate:
        print("\nYou have $" + str(float(money)) + " to allocate.")
        def allocation(word):
            var = input(f"\nHow much money would you like to allocate to your {word} budget?\n$")
            var = isFloat(var)
            return var

        rent = allocation('rent')
        food = allocation('food')
        gas =  allocation('gas')
        spending =  allocation('spending')
        saving =  allocation('saving')
        budgets=[rent,food,gas,spending,saving]
        #If the user’s percentages/number amounts DO NOT add up to 100% of the user’s total money:
        totalBudget = rent + food + gas + spending + saving
        if totalBudget != money:
            #Tell the user that their numbers don’t add up and they need to try again:
            print("\nThose numbers don't add up to your total money!\n\nPlease try again.")
            #Run the budgeting function to keep the program running:
            budgeting(account)

        #If the user’s percentages/number amounts DO add up to 100% of the user’s total money:
        else:

            #Set the user’s new budget in a variable:
            update["rent"] = rent
            update["food"] = food
            update["gas"] = gas
            update["spending"] = spending
            update["saving"] = saving
            
            print(save(account['name'][0],update))

            #Tell the user that the process was successful:
            input("\nYour new budget has been set!")
            return

    #If the user chose to compare expenses to budget:
    if budgetChoice == 2:

        #Ask the user what their expense is:
        expenseThing = input("\nWhat thing are you aiming to buy?\n")

        #Ask the user how much their expense costs:
        expenseCost = input("\nHow much does it cost?\n$")
        expenseCost = isFloat(expenseCost)

        #Ask the user what budget category it applies to:
        category = int_input("\nWhat budget category does your expense apply to? \n1. Rent\n2. Food\n3. Gas\n4.Spending\n5. Saving\n")

        #Make sure the user chose a valid option:
        if category == 1:
            category ='rent'
        elif category == 2:
            category = 'food'
        elif category == 3:
            category = 'gas'
        elif category == 4:
            category = 'spending'
        elif category == 5:
            category = 'saving'
        else:
            print('invalid option')
            budgeting(account)

        #If the user DOES NOT have enough money in their budget for the expense:
        number=float(account[category][-1])
        if expenseCost > number:

            #Tell the user that they do not have enough money, and show them how much more money they still need:
            moneyStillNeeded = expenseCost - number
            input(f"\nYou do not have enough money to purchase the {expenseThing}.\nYou still need an additional ${moneyStillNeeded}.")
            return

        #If the user DOES have enough money in their budget for the expense:
        else:

            #Tell the user that they have enough money, and show them how much they exceeded their expense by:
            moneyExceeded = number - expenseCost
            input(f"You have enough money to purchase the {expenseThing}!\nYou exceeded the amount needed to pay the expense by ${moneyExceeded}.")
            return

    #If the user chose to exit:
    if budgetChoice == 3:

        #Exit this function and return to the main page:
        return

#budgeting(load('test'))
