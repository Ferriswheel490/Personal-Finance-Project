#Cecily Strong income expense handling
import datetime
def income_expense(list):
    inc_exp=[{'date':'','expenses':[],'income':[]}]
    num=int(input("1. Track income\n 2. Track expense\n 3. Compare\n 4. exit"))
    if num == 1:
        amount=int(input('amount'))
        source = int(input('source'))
        inc_exp['income'].append({'amount': amount, 'source': source}) 
    if num == 2:
        amount=int(input('amount'))
        source = int(input('source'))
        inc_exp['expenses'].append({amount: amount, source: source}) 
    if num == 3:
        year=int(input("what year do you want to see finances for?"))
        temp=[]
        for x in list:
            if list[x] == year:
                temp.append(x)
            print(temp) 
    if num == 4:
        return inc_exp
    else:
        print('invalid option') 
        income_expense(list)
