#Cecily Strong income expense handling
from account_handling import *
def income_expense(dic):
    #display(dic) #for debugging
    #inc_exp={'expenses':[],'income':[]}
    if dic==False:
        return False
    else:
        def tracking(amount,source,amount_input,source_input):
            for x in list(dic.keys()):
                if x == amount or x == source: #or x == 'name':
                    pass
                elif x == 'total_funds':
                    if amount=='income_amount':
                        try:
                            dic['total_funds'].append(dic['total_funds'][-1]+float(amount_input))
                        except:
                            dic['total_funds']=[0]
                            dic['total_funds'].append(dic['total_funds'][-1]+float(amount_input))
                    elif amount=='expense_amount':
                        dic['total_funds'].append(dic['total_funds'][-1]-float(amount_input))
                else:
                    dic[x].append('')

            #dic['name'].append(dic['name'])
            dic[amount].append(amount_input) 
            dic[source].append(source_input) 
            return dic
        def latest(dic):
            dic2={}
            for x in list(dic.keys()):
                dic2[x]=dic[x][-1]
            return dic
        
        #decision structure
        num=int(input("1. Track income\n2. Track expense\n3. Compare\n4. exit\n"))
        if num == 1: #track income
            tracking('income_amount','income_source',int(input('amount\n')),input('source\n'))
            new=latest(dic)
            save(dic,new)
            return dic
        if num == 2: #track expenses
            tracking('expense_amount','expense_source',int(input('amount\n')),input('source\n')) 
            save(dic,new)
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
        else: #stupid proofing
            print('invalid option') 
            income_expense(dic)
    



#debug()
print(income_expense(load('a')))
print(income_expense(load('test')))