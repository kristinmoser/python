''' 
cs1114 

Submission: rec11

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
import random


def makeListOfWords():
    fileHandle = open('words.txt' , 'r')
    listOfWords = []
    for line in fileHandle:
        line.strip()
        listOfWords.append(line)
    print (listOfWords)

def makeHTMLFile():
    filename = raw_input("What would you like to call your file?")  + ".html"
    title = raw_input("choose a title: ")
    heading_size = int(raw_input ("choose a heading size between 1-5: "))
    fh = open ('colors.txt' , 'r')
    listOfColors =[]
    for line in fh:
        line.strip()
        listOfColors.append(line)
    randColor = random.choice(listOfColors)
    f = open(filename,'w')
    message = ("""<html>
    <head></head>
    <title> %s </title>
    <body>
    <h%i><b><font color = %s >Red</font> </b></h1>
    </body>
    </html>""" % (title, heading_size, randColor))
    f.write(message)


makeListOfWords()
makeHTMLFile()

        
    
