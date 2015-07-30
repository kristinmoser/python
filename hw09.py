''' 
cs1114 

Submission: hw09

Programmer: Kristin Moser
Username: km3322

Purpose of program, assumptions, constraints:
The program processes so UN data from a file and writes the average, lowest, and highest values
into another file based on its year.

'''

FILENAME_1970 = '1970_1990_summary.txt'
FILENAME_1990 = '1990_2007_summary.txt'
import copy

def getData():
    '''opens the file where the data is stored and seperates the data into dictionaries
    based on the years. the dictionarys' keys are the country names and the values are the percents'''
    fh = open('UNdata.txt' , 'r')
    UNdict1970 = {}
    UNdict1990 = {}
    fh.readline()
    for line in fh:
        country = line.split(",", 1)
        country = country[0]
        year = line.split("\t" , 1)
        year = year[0].split(country + ", ")
        year = year[1]
        percent = line.split("%", 1)
        percent = percent[0].split("\t")
        percent = float(percent[1])
        if year == '1970-1990':
            UNdict1970[country] = percent
        else:
            UNdict1990[country] = percent
    return UNdict1970, UNdict1990

def calcData(dicty):
    total = 0
    lowest = 100
    highest = 0
    for value in dicty.values():
        total += value
        avg = float(total) / len(dicty)
    valueList = []
    for value in dicty.values():
        valueList.append(abs(value))
    valueList.sort()
    lowestVal = valueList[0:3]
    highestVal = valueList[-3:]
    return avg, lowestVal, highestVal

def organizeData(dicty, lowestVal, highestVal):
    lowValue1 = lowestVal[0]
    lowValue2 = lowestVal[1]
    lowValue3 = lowestVal[2]
    highValue1 = highestVal[0]
    highValue2 = highestVal[1]
    highValue3 = highestVal[2]
    return lowValue1, lowValue2, lowValue3, highValue1, highValue2, highValue3
   
def orgCountries( dicty, lowValue1, lowValue2, lowValue3,highValue1, highValue2, highValue3):
    
    inv_dicty = {a: b for b, a in dicty.items()}
    print inv_dicty [lowValue1]
    lowCountry1 = inv_dicty[lowValue1]
    lowCountry2 = inv_dicty[lowValue2]
    lowCountry3 = inv_dicty[lowValue3]
    highCountry1 = inv_dicty[highValue1]
    highCountry2 = inv_dicty[highValue2]
    highCountry3 = inv_dicty[highValue3]
    return lowCountry1, lowCountry2, lowCountry3, highCountry1, highCountry2, highCountry3
    
    
def writeFile(dicty, avg, lowValue1, lowValue2, lowValue3, highValue1, highValue2, highValue3):
    if dicty == UNdict1970:
        fileHandle = open(FILENAME_1970,'w')
    else:
        fileHandle = open(FILENAME_1990, 'w')
    summaryReport = (
        ''' Summary Report\n\n
        Average Percent Overall: %.3f\n
        The three countries or regions with the largest change:\n
        %s(%.2f), %s(%.2f), %s(%.2f)\n
        The three countries with the smallest change:\n
        %s(%.2f), %s(%.2f), %s(%.2f)'''
         %(avg, highCountry1, highValue1, highCountry2, highValue2, highCountry3, highValue3, lowCountry1, lowValue1, lowCountry2, lowValue2, lowCountry3, lowValue3, ))
    print summaryReport
    fileHandle.write(summaryReport)

