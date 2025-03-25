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
                    print(x)
                    acc[x]=acc[x].append(row[li.index(x)])
        return acc
    else: return False
def save(name,update):
    today = datetime.date.today()
    formatted_date = today.strftime("%Y/%m/%d")
    update['date']=formatted_date
    with open(f"{name}.csv","a",newline='') as file:
        writer=csv.DictWriter(file,fieldnames=['name','date','expense','source','amount','income','source','amount','saving goals', 'saving goal amount', 'budget_limits', 'budget_limit_amount'])
        writer.writeheader()
        writer.writerows(update)    
print(load(export('test')))