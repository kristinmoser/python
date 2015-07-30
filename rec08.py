#!/Python27/python.exe
'''
filename: rec08.py
programmer: Kristin Moser
username: km3322
this program draws a number of stars based on the users inputted value. it does not allow the user to input
a negative number of stars. it also creates a list of with a range determined by the user and ever number in that
range raised to an exponent also chosen by the user. the list is printed. then a string of hyphens is produced based
on the numbers in the list. at the end of every hyphen string the number of hyphens is printed at the end.'''

def getUserStars():
    '''asks the user how many starts they want'''
    numStars = int(raw_input ("how many stars do you want?"))
    while not checkIfPositive(numStars):
        numStars = int(raw_input("sorry that was an invalid response. try again." + " "))
    return numStars

def drawStar():
    '''assigns star and returns it'''
    star = '*'
    return star
def drawMultipleStars(numStars, star):
    '''draws a stars based on the number the user inputted'''
    print (star * numStars)

def checkIfPositive(x):
    '''checks if a value is positive'''
    if x > 0:
        return True

def createPowerSeries(start, end, exponent = 2):
    '''creates a list of numbers in a range raised to an exponent'''
    powList=[]
    for i in range (start, end +1):
        powList = [i ** exponent for i in range(start, end + 1)]
    return powList

def getUserValues():
    '''asks the user for starting, ending, and an exponent value and returns them'''
    start = int(raw_input("choose a starting value:"))
    end = int(raw_input("choose an ending value:"))
    exponent = int(raw_input("choose a value for the exponent:"))
    return start, end, exponent

def createHyphen(powList):
    '''puts the number of hyphens according to the number in the list and puts that number in parenthesis at then end of the hyphens'''
    for i in powList:
        print ("-" *i + "(" + (str(i)) + ")")


def main():
    numStars = getUserStars()
    star = drawStar()
    drawMultipleStars(numStars, star)
    start, end, exponent = getUserValues()
    powList = createPowerSeries(start, end, exponent)
    print powList
    createHyphen(powList)

main()
