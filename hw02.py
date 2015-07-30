'''
Programmer: Kristin Moser
username:km3322
filename: hw02.py

this program takes two characters and returns a string
based on those characters ASCII numeric difference. The string is
wrapped around the screen, so that the maximum number of
characters per line is 24.
'''
import math
import __builtin__
def getCheckeredLine(): 
    first_character=raw_input("What character do you want to be the first character?")
    second_character=raw_input("What character do you want to be the second character?")
    num2repeat=abs(ord(first_character)-ord(second_character))
    phrase=first_character+second_character
    checkered_line=phrase*num2repeat
    remainder=num2repeat%12
    number_of_lines=num2repeat/12
    print(phrase*12+"\n")*number_of_lines + phrase*remainder

getCheckeredLine()
    
    
