#Cecily Strong
import csv
import os
from cecilys_helpers import debug
import datetime
def new_acc(name): #note: dont have two accounts have the same name
    if export(name)==False:
        header=['name','date','total_funds','expense_source','expense_amount','income_source','income_amount','amount','saving goals', 'saving goal amount', 'budget_limits', 'budget_limit_amount']
        with open(f"{name}.csv","w",newline='') as file1:
            writer=csv.DictWriter(file1,fieldnames=header)
            writer.writeheader()
            writer.write({'name':[name],'date':[0],'total_funds':[0],'expense_source':[0],'expense_amount':[0],'income_source':[0],'income_amount':[0],'saving goals':[0], 'saving goal amount':[0], 'budget_limits':[0], 'budget_limit_amount':[0]})
        with open(f"code/acc_names.csv","a") as file:
            file.write(f"\n{name}")
        return 'Account successfully created'
    else:
        return 'Account already exists'


def export(acc):
    with open(f"code/acc_names.csv","r") as file:
        reader=csv.reader(file)
        #next(reader)
        for row in reader:
            if row[0] == acc:
                return acc
        else: return False

def load(name):
    if export(name) != False:
        acc={'name':[name],'date':[0],'total_funds':[0],'expense_source':[0],'expense_amount':[0],'income_source':[0],'income_amount':[0],'saving goals':[0], 'saving goal amount':[0], 'budget_limits':[0], 'budget_limit_amount':[0]}
        li=list(acc.keys())
        with open(f"{name}.csv","r",newline='') as file:
            reader=csv.reader(file)
            next(reader)
            for row in reader:
                for x in li:
                    acc[x].append(row[li.index(x)])
        return acc
    else: 
        return False

# NOTE: you can only save one savings goal, budget limit, income, ect at a time. do it every time your function runs before you return, perhaps?
def save(name,update):
    if export(name) == False:
        return False
    else:
        today = datetime.date.today()
        formatted_date = today.strftime("%Y/%m/%d")
        update['name'] = name
        update['date'] = formatted_date
        with open(f"{name}.csv","a",newline='') as file:
            writer=csv.DictWriter(file,fieldnames=['name','date','total_funds','expense_source','expense_amount','income_source','income_amount','amount','saving goals', 'saving goal amount', 'budget_limits', 'budget_limit_amount'])
            writer.writerow(update)

def display(dic):
    if export(dic)==False:
        return False
    else:
        for x in list(dic.keys()):
            print(f"{x}:{dic[x]}")

def purge():
    with open(f"code/acc_names.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        for name in reader:
            os.remove(f"{name[0]}.csv")
    with open(f"code/acc_names.csv","w") as file:
        writer=csv.writer(file)
        writer.writerow(['name'])
#purge()
new_acc('test')
'''
save(export('cecily'),{'name':'cecily','date':'','expense_source':'a','expense_amount':'2','income_source':'c','income_amount':'4','saving goals':'d', 'saving goal amount':'6', 'budget_limits':'f', 'budget_limit_amount':'8'})
'''
#display(load(export('cecily')))
