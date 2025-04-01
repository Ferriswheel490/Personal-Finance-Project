#Cecily Strong income expense handling
import datetime
from account_handling import *
def income_expense(dic):
    #display(dic) #for debugging
    #inc_exp={'expenses':[],'income':[]}

    #helper functions
    def latest(dic):
        dic2={}
        for x in list(dic.keys()):
            dic2[x]=dic[x][-1]
        return dic2
    def tracking(amount,source,amount_input,source_input):
        for x in list(dic.keys()):
            if x == amount or x == source: #or x == 'name':
                pass
            else:
                dic[x].append('')
        #dic['name'].append(dic['name'])
        dic[amount].append(amount_input) 
        dic[source].append(source_input) 
        return dic
    
    #decision structure
    num=int(input("1. Track income\n2. Track expense\n3. Compare\n4. exit\n"))
    if num == 1: #track income
        tracking('income_amount','income_source',int(input('amount\n')),input('source\n'))
        new=latest(dic)
        save(export('cecily'),new)
        return dic
    if num == 2: #track expenses
        tracking('expense_amount','expense_source',int(input('amount\n')),input('source\n')) 
        save(export('cecily'),new)
        return dic
    if num == 3: #compare
        #year=int(input("what year do you want to see finances for?\n"))
        year=2025
        temp=[]
        for x in dic['date']:
            if dic['date'][dic['date'].index(x)][0:3] == str(year):
                print(x)
                temp.append(x)
            print(temp) 
        return dic
    if num == 4: #exit
        return dic
    #''' 
    else: #stupid proofing
        print('invalid option') 
        income_expense(dic)
    #'''

dic=load(export('cecily'))
year=2025
year=str(year)
temp=[]
'''
for x in dic['date']:
    if dic['date'][dic['date'].index(x)][0:4] == str(year):
        temp.append(x)
print(temp) '''
#income_expense(load(export('cecily')))