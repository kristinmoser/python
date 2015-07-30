#!/python/python.exe
''' 
cs1114 

Submission: rec02

Programmer: Kristin Moser
Username: km3322

This program prints a welcome statement
followed by a box with dimensions of 5*7 made of x's with the name joe
inside followed by a thank you statement.

'''
from __future__ import print_function
import os

def displayWelcome():
    ''' prints Welcome on the screen
    '''
    print ( "Welcome" )

def displaySevenXs():
    ''' prints a row of 7 x's'''
    print ( "x"*7 )

def displayTwoXsWithHole():
    ''' prints 2 x's with 5 spaces
    inbetween'''
    print ( "x"+" "*5+"x" )
def displayTwoXsWithJoe():
    '''prints 2 x's with the name joe
    inbetween'''
    print( "x joe x" )
def displayThanks():
    '''prints thankyou on
        the screen'''
    print ( "thank you" )
def drawBox():
    '''combines all functions used to create
    the box in order to draw the box on the screen '''
    displaySevenXs()
    displayTwoXsWithHole()
    displayTwoXsWithJoe()
    displayTwoXsWithHole()
    displaySevenXs()
def main():
    displayWelcome()
    drawBox()
    displayThanks()
    os.system("PAUSE")
if __name__== '__main__':
    main()

