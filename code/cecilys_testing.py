#Cecily Strong testing
from account_handling import *
from income_expense_handling import *
from currency_conversion import*
num=int(input("""
1. make a new account
2. load an account
3. income and expense handling
4. currency conversion
"""))
if num == 1:
    display(load(export(new_acc(input('what is your name?\n')))))
elif num==2:
    display(load(export(input('what is your name?\n'))))
elif num == 3:
    income_expense(load(export(input('what is your name?\n'))))
elif num == 4:
    thing=('',False)
    while thing[1]==False:
        thing=currency_convert(input('what is your first currency (3 leter abbreviation)?'),input('what is your second currency(3 leter abbreviation)?'),input('how much do you want to convert?'))
    else:
        print(thing)