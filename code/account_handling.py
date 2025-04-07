# --------------------------------Cecily--------------------------------------------
import csv
import os
from cecilys_helpers import debug
import datetime
from essentials import cs

# name is just the name for the account you want
# NOTE: dont have two accounts have the same name 
# intended to be used with a print statment
def new_acc(name,password): 
    try:
        exist = export(name)
    except: exist = False
    if exist == False:
        header=['name','date','total_funds','expense_source','expense_amount','income_source','income_amount','amount','saving goals', 'saving goal amount', 'budget_limits', 'budget_limit_amount']
        with open(f"{name}.csv","w",newline='') as file1:
            writer=csv.DictWriter(file1,fieldnames=header)
            writer.writeheader()
            writer.writerow({'name':name,'date':'0','total_funds':'0','expense_source':'0','expense_amount':'0','income_source':'0','income_amount':'0','saving goals':'0', 'saving goal amount':'0', 'budget_limits':'0', 'budget_limit_amount':'0'})
        with open(f"Personal-Finance-Project/code/acc_names.csv","a") as file:
            file.write(f"\n{name},{password}")
        return 'Account successfully created'
    else:
        return 'Account already exists'

# acc is the name of the account you want to fetch, dont use .csv (for example, load('test'))
def export(acc): #this checks if the account exists
    with open(f"Personal-Finance-Project/code/acc_names.csv","r") as file:
        reader=csv.reader(file)
        #next(reader)
        for row in reader:
            try:
                if row[0] == acc:
                    return acc
            except: pass
        else: return False

# name is the name of the account you want to fetch, dont use .csv (for example, load('test'))
def load(name): #this is intended just for fetching a list that you can append to and change
    if export(name) != False:
        acc={'name':[],'date':[],'total_funds':[],'expense_source':[],'expense_amount':[],'income_source':[],'income_amount':[],'saving goals':[], 'saving goal amount':[], 'budget_limits':[], 'budget_limit_amount':[]}
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
# name is the account dictionary, you can just do this easily with the export command and the name
# update is the update you want, so not the entire dictionary, just the latest addition
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


# this is mostly just for cecilys testing. displays the csv nicely
# do NOT use with a print statement. it doesn't cause any errors or anything, its just ugly to see "None"
def display(dic): 
        for x in list(dic.keys()):
            print(f"{x}:{dic[x]}")

def purge(): #deletes ALL accounts. use with caution
    with open(f"Personal-Finance-Project/code/acc_names.csv","r") as file:
        reader=csv.reader(file)
        next(reader)
        for name in reader:
            try:
                os.remove(f"{name[0]}.csv")
            except: pass
    with open(f"Personal-Finance-Project/code/acc_names.csv","w") as file:
        writer=csv.writer(file)
        writer.writerow(['name','password'])

#----------------------JACKSON----------------------------------

USER_FILE = "Personal-Finance-Project/code/acc_names.csv"
#theres a bug when you just have it use code/acc_names now, idk why -Cecily

# Check if CSV file exists, create it if not  
# Hey, you'd never believe this, but I have something for that too. its in new_acc and in export. I don't want reduntant code -Cecily 
'''     
def initialize_file():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Header row
'''

# Load users from CSV into a dictionary
def load_users():
    users = {}
    with open(USER_FILE, "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) == 2:  # Ensure valid data
                users[row[0]] = row[1]
    return users

# Save a new user to the CSV file
# I already had a function handling new accounts, and it made a new csv file for them too, so I am commenting this out -Cecily
'''def save_user(username, password):
    with open(USER_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password])'''

# Sign-in function
def sign_in():
    cs()
    users = load_users()
    while True:
        has_account = input("Do you have an account? (yes/no): ").strip().lower()

        if has_account == "no":
                create = input("Do you want to create one? (yes/no): ").strip().lower()
                if create == "yes":
                    return create_account()
                else:
                    print("Okay, you have to haha...")
                    return False
        elif has_account == 'yes':
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in users and users[username] == password:
                print(f"Login successful! Welcome back, {username}!")
                return load(username)
            else:
                print("Invalid username or password.")
        else: 
            print('invalid option')
            sign_in()

# Account creation function
def create_account():
    username = input("Choose a username: ")
    
    if export(username) != False:
        print("Username already taken. Try again.")
        return create_account()
    else:
        password = input("Choose a password: ")
        print(new_acc(username, password))
        return load(username)

# We need a function that takes username and password and either makes a new account with a setup process or loads the old account into a master list -Jackson
debug()
sign_in()