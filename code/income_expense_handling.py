#Cecily Strong income expense handling
import datetime
from account_handling import *
def income_expense(dic):
    display(dic)
    #inc_exp={'expenses':[],'income':[]}
    def tracking(amount,source):
        amount_input=int(input('amount\n'))
        source_input = input('source\n')
        dic[amount].append(amount_input) 
        dic[source].append(source_input) 
        return dic
    num=int(input("1. Track income\n 2. Track expense\n 3. Compare\n 4. exit\n"))
    if num == 1: #track income
        tracking('income_amount','income_source')
        save(load(export('cecily')),(dic[x][-1] for x in list(dic.keys())))
    if num == 2: #track expenses
        tracking('expense_amount','expense_source') 
        save(load(export('cecily'),dic[-1]))
    if num == 3: #compare
        year=int(input("what year do you want to see finances for?"))
        temp=[]
        for x in dic['date']:
            if dic['date'][x][0:3] == year:
                temp.append(x)
            print(temp) 
    if num == 4:
        return dic
    ''' 
    else:
        print('invalid option') 
        income_expense(list)
    '''
print(income_expense(load(export('cecily'))))