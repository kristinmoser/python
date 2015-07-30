#!C:\Python26\python.exe

'''
Programmer: Kristin Moser
Assignment: rec03

This program prints a reciept for a local coffee and doughnut shop

'''
TAX_RATE=.0846
price_of_one_coffee=.77
price_of_one_doughnut=.64


def displayWelcome():
    '''displays a welcome message on the screen'''
    print ("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\")
    print ("THE COFFEE AND DOUGHNUT SHOPPE")
    print ("\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
def getOrder():
    ''' asks the user for their order'''
    coffee_num=int(raw_input("How many cups of coffee would you like?"))
    doughnut_num=int(raw_input("How many doughnuts would you like?"))
    return coffee_num, doughnut_num
def calculatePrice (coffee_num, doughnut_num):
    '''calculates the total doughnut price and total coffee price'''
    doughnut_price=float(doughnut_num*price_of_one_doughnut)
    coffee_price=float(coffee_num*price_of_one_coffee)
    total=coffee_price+doughnut_price
    return coffee_price, doughnut_price, total
def calculateTax(total, TAX_RATE):
    ''' calculates the tax added to the coffee price and doughnut price'''
    tax=total*TAX_RATE
    return tax
def calculateTotalwithTax(tax, total):
    '''calculates the total order price with the tax'''
    TotalwithTax= total+tax
    return TotalwithTax
def PrintReciept(coffee_num, coffee_price, doughnut_num, doughnut_price, tax, TotalwithTax):
        ''' displays the reciept'''
        displayWelcome()
        print ("%i cups of coffee: $%.2f"%(coffee_num, coffee_price))
        print ("%i doughnuts: $%.2f"%(doughnut_num, doughnut_price))
        print ("tax: $%.2f"%(tax))
        print ("Amount Owed: $%.2f"%(TotalwithTax))
def displayThanks():
    '''displays a thank you message on the screen'''
    print ("Thanks for buying local!")
def pause():
    '''pauses the program'''
    raw_input("Press any key to continue...")
def main():
    ''' prints the reciept and pauses the program'''
    coffee_num,doughnut_num=getOrder()
    coffee_price,doughnut_price,total=calculatePrice(coffee_num, doughnut_num)
    tax=calculateTax(total, TAX_RATE)
    TotalwithTax=calculateTotalwithTax(tax, total)
    PrintReciept(coffee_num, coffee_price, doughnut_num, doughnut_price, tax, TotalwithTax)
    displayThanks()
    pause()

main()
