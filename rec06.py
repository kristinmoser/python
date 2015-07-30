#!C:\python27\python.exe
'''
Programmer: Kristin Moser
username: km3322
file_name= rec06.py

This program is a stamp machine that runs forever unless exited by
the manager or chris martin. It also takes tip from the user if they
input too much money and only returns coins. 
'''


import moneychanger
import random
SEVENTY_FOUR_CENT_STAMP=0.74
THIRTY_TWO_CENT_STAMP=0.32
SIX_CENT_STAMP=0.6
CUSTOMERS=0


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
    first_name= str(raw_input("What is your first name?"))
    last_name= str(raw_input("What is your last name?"))
    return first_name, last_name

def checkValue(stamp):
    '''checks if the number of stamps is negative'''
    while (stamp<0):
        stamp=int(raw_input("That is a negative number. Input a positive number."))
    return stamp

def getCustomersStampOrder():
    '''asks the user how many of each stamp they want'''
    stamps_of_74=int(raw_input("How many 74 cent stamps do you want?"))
    stamps_of_74 = checkValue(stamps_of_74)
    stamps_of_32=int(raw_input("How many 32 cent stamps do you want?"))
    stamps_of_32 = checkValue(stamps_of_32)
    stamps_of_6=int(raw_input("How many 6 cent stamps do you want?"))
    stamps_of_6 = checkValue(stamps_of_6)
    return stamps_of_74, stamps_of_32, stamps_of_6
                          
def calcPrice(stamps_of_74,stamps_of_32,stamps_of_6):
    '''calculates the total number of stamps and th price of all the stamps the user wants''' 
    total_price= (stamps_of_74*SEVENTY_FOUR_CENT_STAMP)+ (stamps_of_32*THIRTY_TWO_CENT_STAMP)+ (stamps_of_6*SIX_CENT_STAMP) 
    total_stamps= stamps_of_74 + stamps_of_32 + stamps_of_6
    return total_price, total_stamps

def calcChange(dollars,total_price):
    '''calculates the change after the user inputs money'''
    change=dollars -(total_price)
    return change
def calcNewChange (tip, change):
    '''calculates a new change if tip is taken out'''
    if tip:
        change = abs(change - tip)
    return change  
def calcChangeAsCoins(change):
    ''' calculates the change in coin form'''
    dollar_coins, quarters, dimes, nickels, pennies = moneychanger.quantityOfCoins(change)
    return dollar_coins, quarters, dimes, nickels, pennies

def displayChange(first_name, last_name, dollar_coins, quarters, dimes, nickels, pennies, total_stamps, total_price, dollars, change):
    ''' displays the total change and the change as coins'''
    print ("Your change is $%0.2f" % (change))
    moneychanger.printAsCoins(dollar_coins, quarters, dimes, nickels, pennies)

def printAmountOwed(total_price):
    '''displays the amount the user owes'''
    print("You owe $%0.2f" % (total_price))
    
def getCustomersDollarInput(total_price):
    '''asks the user how many dollars they are inputing'''
    dollars=int(raw_input("How many dollar bills are you putting into the machine?"))
    while dollars < total_price:
        print ("That's not enough money! Please input more money.")
        new_dollars = int(raw_input("How many dollar bills are you putting into the machine?"))
        dollars = dollars + new_dollars
    return (dollars)
def stealDollarsAsTip(dollar_coins):
    '''calculates the tip recieved by the machine'''
    tip = dollar_coins
    print ("Thanks for the $%i tip, sucker." % (tip))
    return tip

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
def pause(customers, sumOfPurchases, maxTotalPrice, minTotalPrice, numSame):
    '''displays a summary of the machines stats and exits the program'''
    avgPurchase = sumOfPurchases / customers
    percentSame = str(((float(numSame) / customers) * 100)) + "%"
    print ("~~~~~~~~~~~~~~~~stat report~~~~~~~~~~~~~~~~")
    print ("total customers = %i" % (customers))
    print ("average purchase = $%.2f" % (avgPurchase))
    print ("maximum purchase = $%.2f" % (maxTotalPrice))
    print ("minimum purchase = $%.2f" % (minTotalPrice))
    print ("percent of customers who bought the\nsame number of 32 cent stamps as\nany other stamps = %s " % (percentSame))
    print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    raw_input("Do your maintainace work \n ...and... \ndon't forget to restart this program.")
    exit()

def middleExitWithName(first_name, last_name, customers, sumOfPurchases, maxTotalPrice, minTotalPrice, numSame):
    '''the program exits if the user is the manager or chris martin'''
    if first_name == "MANAGER" and last_name == "MANAGER":
        pause(customers, sumOfPurchases, maxTotalPrice, minTotalPrice, numSame)
    elif first_name== "CHRIS" and last_name== "MARTIN":
        pause(customers, sumOfPurchases, maxTotalPrice, minTotalPrice, numSame)
  
        
def processOneStampMachineCustomer(customers, sumOfPurchases, maxTotalPrice, minTotalPrice, numSame):
    '''calls all the functions that are used to process one stamp
    machine customer'''
    print ("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
    displayRandomBannerLine()
    displayRandomBannerLine()
    displayRandomBannerLine()
    print("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
    displayWelcomeBanner()
    first_name, last_name = getCustomersName()
    middleExitWithName(first_name, last_name, customers, sumOfPurchases, maxTotalPrice, minTotalPrice, numSame)
    stamps_of_74,stamps_of_32,stamps_of_6 = getCustomersStampOrder()
    total_price, total_stamps = calcPrice(stamps_of_74,stamps_of_32,stamps_of_6)
    print "Your total is $%0.2f" %(total_price)
    dollars = getCustomersDollarInput(total_price)
    change = calcChange(dollars,total_price)
    dollar_coins, quarters, dimes, nickels, pennies = calcChangeAsCoins(change)
    tip = stealDollarsAsTip(dollar_coins)
    change = calcChange(dollars,total_price)
    change = calcNewChange(change, tip)
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
    total_price = total_price
    stamps_of_74 = stamps_of_74
    stamps_of_32 = stamps_of_32
    stamps_of_6 = stamps_of_6
    return total_price, stamps_of_74,stamps_of_32,stamps_of_6
 
def main():
    customers = 0
    sumOfPurchases = 0
    maxTotalPrice = 0
    minTotalPrice = 100
    numSame = 0
    while(True):
        total_price,stamps_of_74,stamps_of_32,stamps_of_6 = processOneStampMachineCustomer(customers, sumOfPurchases, maxTotalPrice, minTotalPrice, numSame)
        customers += 1
        sumOfPurchases += float(total_price)
        if total_price > maxTotalPrice:
            maxTotalPrice = total_price
        if total_price < minTotalPrice:
            minTotalPrice = total_price
        if stamps_of_32 == stamps_of_74:
            numSame += 1
        elif stamps_of_32 == stamps_of_6:
            numSame += 1


    
        
main()

    
