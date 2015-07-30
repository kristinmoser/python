''' 
cs1114 

Submission: hw10

Programmer: Kristin Moser
Username: km3322

Purpose of program, assumptions, constraints:

The program level documentation goes here
What the program does
Any special tricks
Any assumtions
Any constraints
etc..

'''

import copy

def displayList(someList):
    '''displays the elements in a passed in list, one at a time'''
    for i in someList:
        print(i)

def returnMinValue(someList):
    '''returns the minimum value in a passed in list'''
    minValue = min(someList)
    return minValue

def returnIndexOfMin(someList):
    '''returns the index of the minimum value in a passed in list'''
    minValue = returnMinValue(someList)
    indexOfMin = someList.index(minValue)
    print ("index of min" + str(indexOfMin))
    return indexOfMin

def chopOutSequence(someList, val1, val2):
    '''removes values from someList and returns the new list'''
    removeList = copy.deepcopy(someList)
    removeList[val1-1:val2] = []
    print ("Remove list" + str(removeList))
    return removeList

def getCommonElements(someList, someOtherList):
    '''takes two lists and returns a list of those elements that both have
    in common'''
    commonVal=[]
    for i in range(len(someList)):
        if someList[i] in someOtherList: #and value not in commonVal:
            commonVal.append(someList[i])
    print ("common val" + str (commonVal))
    return commonVal
        

def reorderSpliceAndReturn(someList, someOtherList):
    '''    takes two lists and reorders the first list into descending numeric
    order, then splices the second list's elements into the first list
    and returns that list. '''
    addList = copy.deepcopy(someList)
    addList.sort(reverse = True)
    minValSomeOtherList = returnMinValue (someOtherList)
    counter = 0
    print ("minvalue" + str(minValSomeOtherList))
    while((counter < len(someOtherList)) and (minValSomeOtherList <= addList[counter])):
        counter+=1
    addList[counter:counter] = someOtherList
    print ("add list" + str(addList))

    return addList

def main():
    lst = [12, 1, 2, 5]
    lst2 = [2, 3, 4, 6]
    displayList(lst)
    minValue = returnMinValue(lst)
    indexOfMin = returnIndexOfMin(lst)
    chopOutSequence(lst, 1, 2)
    commonVal = getCommonElements(lst, lst2)
    addList = reorderSpliceAndReturn(lst, lst2)

main()

    
