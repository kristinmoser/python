'''
Programmer:Kristin Moser
username:km3322
filename: moneychanger.py
'''
CONVERSION_RATE=0.074
DOLLAR_COIN=1.0
QUARTER_COIN=0.25
DIME_COIN=0.10
NICKEL_COIN=0.05
PENNY_COIN=0.01

def printAsUSDollars (dollars):
    ''' takes a given amount of money
    and prettyprints the amount in
    $9999.99 form'''
    print ("$%.2f" % dollars)

def convertPesosToUSDollars(pesos):
    dollars=CONVERSION_RATE*pesos
    return dollars

def quantityOfCoins (change):
    dollar_coins = change // DOLLAR_COIN
    remain_after_dollars = change % DOLLAR_COIN
    quarters = remain_after_dollars // QUARTER_COIN
    remain_after_quarters = remain_after_dollars % QUARTER_COIN
    dimes = remain_after_quarters // DIME_COIN
    remain_after_dimes = remain_after_quarters % DIME_COIN
    nickels = remain_after_dimes // NICKEL_COIN
    remain_after_nickels = remain_after_dimes % NICKEL_COIN
    pennies = remain_after_nickels // PENNY_COIN
    return dollar_coins, quarters, dimes, nickels, pennies

def printAsCoins (dollar_coins, quarters, dimes, nickels, pennies):
    print ("Here is your change:")
    if dollar_coins > 0:
        print (" %i dollar coin(s)" % (dollar_coins))
    if quarters > 0:
        print (" %i quarter(s)" % (quarters))
    if dimes > 0:
        print (" %i dime(s)" % (dimes))
    if nickels > 0:
        print (" %i nickel(s)" % (nickels))
    if pennies > 0:    
        print ( "%i pennie(s)" % (pennies))
        

    
