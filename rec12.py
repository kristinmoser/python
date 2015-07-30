#!C:\Python26\python.exe
''' 
cs1114 

Submission: rec12

Programmer: Kristin Moser
Username: km3322

Purpose of program:

contraints:
assumptions:

'''
import os
#part 1

def validate(fileName):
    while not os.path.exists(fileName):
        fileName = raw_input("that's not a real file. what file are you opening?")

def getInputFileName():
    fileName = raw_input("what file are you opening?")
    validate(fileName)
    fileHandle = open(fileName , 'r')

    return fileHandle

def getOutputFileName():
    outputFile = raw_input("what file are you writing in?")
    if not validate(outputFile):
        ok = raw_input ("is it okay to overwrite? (Y/N) ")
    fh = open(outputFile, 'w+')
    return ok , fh, outputFile

def splitAndJoin(fh, fileHandle, betweenString, ok):
    if ok == 'Y':
        lst = []
        for line in fileHandle:
            lst.extend(line.split())
        message = betweenString.join(lst)
        fh.write(message)
    else:
        getOutputFileName()
    return lst
    
def pickBetweenString():
    betweenString = raw_input("pick a between string: ")
    return betweenString

def processFile():
    fileHandle = getInputFileName()
    betweenString = pickBetweenString()
    ok, fh, outputFile = getOutputFileName()
    lst = splitAndJoin(fh, fileHandle, betweenString, ok)
    #doOppositeOfPartOne(fileHandle, betweenString, ok, outputFile)
    

#part2

#def doOppositeOfPartOne(fileHandle, betweenString, ok, outputFile):
    #fh = open(outputFile, 'r+')
    #if ok == 'Y':
        #lst = []
        #for line in fh:
            #lst.extend(line.split(betweenString))
        #message = ' '.join(lst)
        #fh.write(message)
    #else:
        #getOutputFileName()

#.split(betweenString)
#' '.join(lst)
processFile()


#part3

#input file is lists
#first int is proj numbers
#create dict [proj number] = avg

#part4
#get copy of part 3
#go to output file
#check if project number has 7
#put in rejects if no 7
