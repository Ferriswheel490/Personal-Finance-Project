# Evan - Budgeting

#Budgeting Function:
def budgeting():

    #Inner function to check if a variable is an integer, and, if so, make it an integer:
    def isInt(var):
        try:
            var = int(var)
        except:
            print("\nINVALID INPUT\n\nPlease try again.")
            budgeting()

    #Ask the user if they want to set budget limits or compare expenses to budget:
    budgetChoice = input("\nWould you like to set budget limits or compare an expense to your budget?\n1. new budget\n2. compare expense to budget\n3. exit\n")

    #Make sure that the user input a valid option:
    isInt(budgetChoice)
    if budgetChoice != 1 and budgetChoice != 2 and budgetChoice != 3:
        print("\nThat's not an option!\n\nPlease try again.")
        budgeting()

    #If the user chose to set budget limits:
    if budgetChoice == 1:

        #Tell the user what the budgeting categories are(Rent, Food, Gas, Spending, Saving):
        print("\nThe categories are as follows:\nRent, Food, Gas, Spending, Saving")

        #Tell the user how much total money they have to allocate:

        #Ask the user how much money they want to allocate to their rent budget(N/A, number amount, or percentage):
        newRentBudget = input("\nHow much money would you like to allocate to your rent budget?\n1. Dollar Amount\n2. Percentage\n")
        isInt(newRentBudget)

        #Ask the user how much money they want to allocate to their food budget(N/A, number amount, or percentage):

        #Ask the user how much money they want to allocate to their gas budget(N/A, number amount, or percentage):

        #Ask the user how much money they want to allocate to their spending budget(N/A, number amount, or percentage):

        #Ask the user how much money they want to allocate to their saving budget(N/A, number amount, or percentage):

        #If the user’s percentages/number amounts DO NOT add up to 100% of the user’s total money:

            #Tell the user that their numbers don’t add up and they need to try again:

            #Run the budgeting function to keep the program running:

        #If the user’s percentages/number amounts DO add up to 100% of the user’s total money:

            #Set the user’s new budget in a variable:

            #Tell the user that the process was successful:

    #If the user chose to compare expenses to budget:

        #Ask the user what their expense is:

        #Ask the user how much their expense costs:

        #Ask the user what budget category it applies to:

        #If the user DOES NOT have enough money in their budget for the expense:

            #Tell the user that they do not have enough money, and show them how much more money they still need:

        #If the user DOES have enough money in their budget for the expense:

            #Tell the user that they have enough money, and show them how much they exceeded their expense by:

    #If the user chose to exit:
    if budgetChoice == 3:

        #Exit this function and return to the main page:
        pass
    