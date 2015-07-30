from __future__ import print_function
import moneychanger
def getPesos():
    pesos=float(raw_input("How many pesos would you like to convert?"))
    return pesos
def main():
    pesos = getPesos()
    dollars = moneychanger.convertPesosToUSDollars(pesos)
    moneychanger.printAsUSDollars(dollars)
    dollar_coins, quarters, dimes, nickels, pennies, totalNoOfCoins = moneychanger.quantityOfCoins(dollars)
    moneychanger.printAsCoins(dollar_coins, quarters, dimes, nickels, pennies,totalNoOfCoins)

main()
                
