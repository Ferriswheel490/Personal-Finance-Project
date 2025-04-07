#Cecily Strong currency conversion
import math  


def main(): # Main function for converting currency
    currencies = {  
    'USD': 1,  
    'EUR': 1.08,  
    'JPY': 0.0066,   
    'GBP': 1.29,  
    'CNH': 0.138218,  
    'AUD': 0.63,  
    'CAD': 0.70,  
    'CHF': 1.14,  
    'HKD': 0.13,  
    'NZD': 0.58  } # List of different currencies and their relation to the USD dollar
    for x in list(currencies.keys()):
        print(x)
    currency1 = input("what currency do you want?") # Inputs for the user
    currency2 = input("what currency do you want?")
    amount = input("how much do you want?")
    def currency_convert(currency1,currency2,amount):     
        currency1=currency1.upper()
        currency2=currency2.upper()
        try: # Error handling
            amount=float(amount)
            if amount>0:
                if currency1 in list(currencies.keys()) and currency2 in list(currencies.keys()):
                    amount=(currencies[currency1]*amount)/currencies[currency2] # conversion equation (converts to usd then the other currency)
                    amount=math.floor(amount*100)/100 # rounds down
                    return (f"{amount} {currency2}")
                else: return 'invalid currency',False
            else:
                return 'invalid amount',False # Checking for invalid amount of mo
        except: return 'not a number',False # Checking for not a number
    output=currency_convert(currency1,currency2,amount)
    if output(1)==False: main()
    else: print(output)
    return


