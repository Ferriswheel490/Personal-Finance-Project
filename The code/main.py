# Cecily/Evan/Hasan/Jackson - Main File

from essentials import * # Imports cs() (clear screen), int_input() (for integer inputs error handling), end(message) ends the program wiht a message
import os
#this may be temporary
def sign_in(username, password, user_database, account, make_account):
    account =  input("do you have an account (y/n): ")
    if account == "yes":
        username_input = input("Username: ")
        password_input = input("Password: ")
        result = sign_in(username_input, password_input)
        print(result)
    elif account == "no":
        make_account = input("do you wanna make an account (y/n): ")
        if make_account == "no":
            return sign_in()
        elif make_account == "yes":
            username_input = input("Username: ")
            password_input = input("Password: ")    