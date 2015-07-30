#!/Python27/python.exe
'''
Programmer: Kristin Moser
username: km3322
filename:rec05.py

This program asks the user how many stamps they want, the user pays, and
then the program returns change back to them. At the end of the program
the user is asked to rate the program and is able to win a prize based on their
purchase and/or the rating they gave.

'''
import moneychanger
import random
SEVENTY_FOUR_CENT_STAMP=0.74
THIRTY_TWO_CENT_STAMP=0.32
SIX_CENT_STAMP=0.6


def displayRandomBannerLine():
    '''displays a banner containing random letters '''
    fill_character = "<"
    phrase1=(chr(random.randrange(97, 124))*random.randint(4,6))
    phrase2=(chr(random.randrange(97, 124))*random.randint(4,6))
    phrase3=(chr(random.randrange(97, 124))*random.randint(4,6))
    phrase4=(chr(random.randrange(97, 124))*random.randint(4,6))
    phrase5=(chr(random.randrange(97, 124))*random.randint(4,6))
    line_with_4_phrases = phrase1+phrase2+phrase3+phrase4
    line_with_5_phrases = phrase1+phrase2+phrase3+phrase4+phrase5
    if random.randint(4,5)==4:
        line = line_with_4_phrases
    else:
        line = line_with_5_phrases

    if len(line)==30:
        print line
    else:
        print (line+ fill_character*(30-len(line)))


def displayWelcomeBanner():
    '''displays welcome banner for the stamp machine'''
    print ("--------------------------------------------\n|     Welcome to the snakeStamp Machine!     |\n| We dispense only 74, 32 and 6 cent stamps. |\n| We give only coins in change - (no bills). |\n--------------------------------------------")

def getCustomersName():
    ''' get users first and last name and returns them'''
    first_name= raw_input("What is your first name?")
    last_name= raw_input("What is your last name?")
    return first_name, last_name

def getCustomersStampOrder():
    '''asks the user how many of each stamp they want'''
    stamps_of_74=int(raw_input("How many 74 cent stamps do you want?"))
    stamps_of_32=int(raw_input("How many 32 cent stamps do you want?"))
    stamps_of_6=int(raw_input("How many 6 cent stamps do you want?"))
    return stamps_of_74, stamps_of_32, stamps_of_6

def calcPrice(stamps_of_74,stamps_of_32,stamps_of_6):
    '''calculates the total number of stamps and th price of all the stamps the user wants''' 
    total_price= (stamps_of_74*SEVENTY_FOUR_CENT_STAMP)+ (stamps_of_32*THIRTY_TWO_CENT_STAMP)+ (stamps_of_6*SIX_CENT_STAMP) 
    total_stamps= stamps_of_74 + stamps_of_32 + stamps_of_6
    return total_price, total_stamps

def calcChange(dollars,total_price):
    '''calculates the change after the user inputs money'''
    change=dollars-total_price
    return change

def calcChangeAsCoins(change):
    ''' calculates the change in coin form'''
    dollar_coins, quarters, dimes, nickels, pennies = moneychanger.quantityOfCoins(change)
    return dollar_coins, quarters, dimes, nickels, pennies

def displayChange(first_name, last_name, dollar_coins, quarters, dimes, nickels, pennies, total_stamps, total_price, dollars, change):
    ''' displays the total change and the change as coins'''
    print ("Your change is $%0.2f" % (change))
    print ("Your change will be given in %i dollar coins, %i quarters, %i dimes, %i nickels, %i pennies" % (dollar_coins, quarters, dimes, nickels, pennies))

def printAmountOwed(total_price):
    '''displays the amount the user owes'''
    print("You owe $%0.2f" % (total_price))
    
def getCustomersDollarInput():
    '''asks the user how many dollars they are inputing'''
    dollars=int(raw_input("How many dollar bills are you putting into the machine?"))
    return dollars

def ThankYou():
    '''displays a thank you message for using the stamp machine'''
    print ("---=======================================---\n--- Thank you for using our stamp machine ---\n---=======================================---")

def getUserRating():
    '''asks the user how it would rate this program'''
    rating=int(raw_input("How would you rate this program?"))
    return rating

def prizeWinnings(rating, total_price):
    '''calculates which of the four prizes the user won'''
    if rating==random.randint(1,1000):
        print "You won the GRAND PRIZE of $50"
    elif rating in (2,4,7) or (total_price >=17.25 and total_price <=58.42):
        print "You won the FIRST PRIZE of $2.33"
    elif total_price > 1.37:
        print ("You won the SECOND PRIZE of $0.37")
    else:
        print ("You won the CONSOLATION PRIZE of $.03")

def reportNumCustomers(customers):
    if customers == 1:
        print ("Today %i customer used this machine" % customers)
    else:
        print ("Today %i customers used this machine" % customers)
    
def runMachineForOneCustomer():
    print ("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
    displayRandomBannerLine()
    displayRandomBannerLine()
    displayRandomBannerLine()
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    displayWelcomeBanner()
    first_name, last_name = getCustomersName()
    stamps_of_74,stamps_of_32,stamps_of_6 = getCustomersStampOrder()
    total_price, total_stamps = calcPrice(stamps_of_74,stamps_of_32,stamps_of_6)
    print "Your total is $%0.2f" %(total_price)
    dollars = getCustomersDollarInput()
    printAmountOwed(total_price)
    change = calcChange(dollars,total_price)
    dollar_coins, quarters, dimes, nickels, pennies = calcChangeAsCoins(change)
    displayChange(first_name, last_name, dollar_coins, quarters, dimes, nickels, pennies, total_stamps, total_price, dollars, change)
    ThankYou()
    rating = getUserRating()
    prizeWinnings(rating, total_price)
    print ("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
    displayRandomBannerLine()
    displayRandomBannerLine()
    displayRandomBannerLine()
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")

def main():
    customers = 0
    while True:
        runMachineForOneCustomer()
        customers += 1
    return customers

main()
        
    
    


    
