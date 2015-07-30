#!C:\Python26\python.exe
''' 
cs1114 

Submission: hw03

Programmer: Kristin Moser
Username: km3322

Purpose of program, assumptions, constraints:

This program plays the game Hit && Match. It assigns random digits
to three positions left, right, and middle and then the user inputs three values
for the three values. the program then calculates if there are any hits or matches.
A hit is if the user's input for a certain position is the same for the house's assigned value
for that position. A match is when any digit inputted by the user matches any of the house's
digits for any position. It prints how many hits and matches. Then a goodbye message is displayed.
The program runs forever until the user presses ^C or an error occurs.

contraints: the house cannot have two digits of the same value; if it does, the program will print an error on the screen and exit the program.
            the user cannot input tow digits of the same value; if it does, the program will print a goodbye message and move onto the next user.

assumptions: the user understands what a digit is and will not input an integer of more than 9
             the user will not input a string value for the left, right, and middle positions
             the user knows what a hit and miss are (they are not explained to the user only in the docstrings)
             
'''
import os
import random

def getHouseDigits():
    '''assigns random digits to positions left, right, and middle and calls
    two functions that check if these digits are the same. if the digits are the same
    the program kills'''
    left = random.randint(0,9)
    middle = random.randint(0,9)
    right = random.randint(0,9)
    if checkIfAllSame(left, middle, right):
        print("We are sorry but the game has malfunctioned. \n Ending... \n \nTraceback ...\n...\nSystemExit: -777777")
        exit()
    if checkIfTwoSame(left, middle, right):
        print("We are sorry but the game has malfunctioned. \n Ending... \n \nTraceback ...\n...\nSystemExit: -777777")
        exit()
    return left, middle, right

def checkIfTwoSame(value1, value2, value3):
    '''checks if any two values are the same in a trio of values'''
    if value1 == value2:
        return True
    elif value1 == value3:
        return True
    elif value2 == value3:
        return True

def checkIfAllSame(value1, value2, value3):
    '''checks if all three values are the same'''
    if value1 == value2 == value3:
        return True

def getUsersDigits():
    '''asks user for three digits to correspond with three positions
    and calls two functions to see if all are the same and if any pair
    are the same. if any digits are the same, the program moves onto the
    next user'''
    user_left = int(raw_input("Enter digit for left position:"))
    user_middle = int(raw_input("Enter digit for middle position:"))
    user_right = int(raw_input("Enter digit for right position:"))
    if checkIfAllSame(user_left, user_middle, user_right):
        print ("Sorry, that is an invalide try.")
        displaygoodbyeMessage()
        playOneHitAndMatchGame()
    if checkIfTwoSame(user_left, user_middle, user_right):
        print ("Sorry, that is an invalid try.")
        displaygoodbyeMessage()
        playOneHitAndMatchGame()
    return user_left, user_middle, user_right   

def calcHits(left, middle, right, user_left, user_middle, user_right):
    '''calculates the number of hits. hits are if the house's number for a certain
    position matches the exact number the user put inputted for that position'''
    hits = 0
    if left == user_left:
        hits = hits + 1
    if middle == user_middle:
        hits = hits + 1
    if right == user_right:
        hits = hits + 1
    return hits

def calcMatches(left, middle, right, user_left, user_middle, user_right):
    '''calculates the number of matches. matches are if any number inputted for any
    position by the user matches any number in any house position'''
    matches = 0
    if left == user_left or left == user_middle or left == user_right:
        matches = matches + 1
    if middle == user_left or middle == user_middle or middle == user_right:
        matches = matches + 1
    if right == user_left or right == user_middle or right == user_right:
        matches = matches + 1
    return matches

def displayHitsAndMatches(hits, matches):
    ''' displays the hits and matches grammatically correct'''
    if hits == 1:
        print ("%i hit" % (hits))
    else:
        print ("%i hits" % (hits))
    if matches == 1:
       print ("%i match" % (matches))
    else:
        print ("%i matches" % (matches))

def pause():
    '''pauses the program with a welcome message'''
    raw_input("Welcome to the Hit && Match Game\nhit any key to start playing...")

def displaygoodbyeMessage():
    '''displays a goodbye message on the screen'''
    print ("Come back and play again sometime\n")

def playOneHitAndMatchGame():
    '''plays the hit and match game once for one user'''
    pause()
    left, right, middle = getHouseDigits()
    user_left, user_right, user_middle = getUsersDigits()
    hits = calcHits(left, middle, right, user_left, user_middle, user_right)
    matches = calcMatches(left, middle, right, user_left, user_middle, user_right)
    displayHitsAndMatches(hits, matches)
    displaygoodbyeMessage()

def main():
    while (True):
        playOneHitAndMatchGame()

main()



