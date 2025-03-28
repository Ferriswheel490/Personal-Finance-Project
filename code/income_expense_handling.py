#Cecily Strong income expense handling
import datetime
def income_expense(list):
    #def tracking()
    inc_exp=[{'expenses':[],'income':[]}]
    num=int(input("1. Track income\n 2. Track expense\n 3. Compare\n 4. exit"))
    if num == 1: #track income
        amount=int(input('amount'))
        source = int(input('source'))
        inc_exp['income'].append({'amount': amount, 'source': source}) 
    if num == 2: #track expenses
        amount=int(input('amount'))
        source = int(input('source'))
        inc_exp['expenses'].append({'amount': amount, 'source': source}) 
    if num == 3: #compare
        year=int(input("what year do you want to see finances for?"))
        temp=[]
        for x in list:
            if list[x][0:3] == year:
                temp.append(x)
            print(temp) 
    if num == 4:
        return inc_exp
    else:
        print('invalid option') 
        income_expense(list)


