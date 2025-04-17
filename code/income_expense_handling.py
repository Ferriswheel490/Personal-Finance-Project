#Cecily Strong income expense handling
from account_handling import *
from essentials import int_input
def income_expense(dic):
    funds=0
    for x in dic['total_funds']:
        print(x)
        if len(x)>0:
            funds=x
    #display(dic) #for debugging
    #inc_exp={'expenses':[],'income':[]}
    update={'name':'','date':'','total_funds':'','expense_source':'','expense_amount':'','income_source':'','income_amount':'', 'budget_limits':'', 'budget_limit_amount':'','rent':'','food':'','gas':'','saving':'','spending':''}
    if dic==False:
        return False
    else:
        
        #decision structure
        num=int(input("1. Track income\n2. Track expense\n3. Compare\n4. exit\n"))
        if num == 1: #track income
            amount=int_input('amount\n')
            source=input('source\n')
            update['income_amount']=amount
            update['income_source']=source
            
            #print(float(funds)+float(amount))
            update['total_funds']=(float(funds)+float(amount))
            input(save(dic['name'][0],update))
            return dic
        if num == 2: #track expenses
            amount=int_input('amount\n')
            source=input('source\n')
            update['expense_amount']=amount
            update['expense_source']=source
            #update['total_funds']=(float(funds)-float(amount))
            input(save(dic['name'][0],update))
            return dic
        if num == 3: #compare

            year=int_input("what year do you want to see finances for?\n")
            number=0
            for x in dic['date']:
                if x[0:4] == str(year):
                    if dic['income_source'][number] != '':
                        print(f"{dic['income_source'][number]}: ${dic['income_amount'][number]}")
                    elif dic['expense_source'][number] != '':
                        print(f"{dic['expense_source'][number]}: ${dic['expense_amount'][number]}")
                number+=1
            input('Press Enter to Exit')
            return 
        if num == 4: #exit
            return 
        else: #stupid proofing
            print('invalid option') 
            income_expense(dic)
    


#income_expense(load('test'))
#debug()
'''
print(income_expense(load('a')))
print(income_expense(load('test')))'''