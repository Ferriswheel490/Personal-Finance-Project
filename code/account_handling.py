#Cecily Strong
import csv
from cecilys_helpers import debug
import datetime
def new_acc(name): #note: dont have two accounts have the same name
    header=['name','date','expense','source','amount','income','source','amount','saving goals', 'saving goal amount', 'budget_limits', 'budget_limit_amount']
    with open(f"{name}.csv","w",newline='') as file1:
        writer=csv.DictWriter(file1,fieldnames=header)
        writer.writeheader()
    with open(f"code/acc_names.csv","a") as file:
        file.write(f"\n{name}")
    return name


def export(acc):
    with open(f"code/acc_names.csv","r") as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0] == acc:
                return acc
        else: return False
def load(name):
    if name != False:
        acc={'name':[],'date':[],'expense':[],'source':[],'amount':[],'income':[],'source':[],'amount':[],'saving goals':[], 'saving goal amount':[], 'budget_limits':[], 'budget_limit_amount':[]}
        li=list(acc.keys())
        with open(f"{name}.csv","r",newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                for x in li:
                    acc[x].append(row[li.index(x)])
        return acc
    else: return False

# NOTE: you can only save one savings goal, budget limit, income, ect at a time. do it every time your function runs before you return, perhaps?
def save(name,update):
    today = datetime.date.today()
    formatted_date = today.strftime("%Y/%m/%d")
    update['date']=formatted_date
    with open(f"{name}.csv","a",newline='') as file:
        writer=csv.DictWriter(file,fieldnames=['name','date','expense','source','amount','income','source','amount','saving goals', 'saving goal amount', 'budget_limits', 'budget_limit_amount'])
        writer.writerow(update)

dic={'name':'test','date':'','expense':'z','source':'f','amount':1,'income':2,'source':'h','amount':1,'saving goals':'g', 'saving goal amount':1, 'budget_limits':1, 'budget_limit_amount':1}

save('test',dic)
load(export('test'))
