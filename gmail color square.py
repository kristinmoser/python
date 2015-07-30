'''
hw01
Kristin Moser
km3322
color square with letter
'''
from PIL import Image, ImageDraw, ImageFont, ImageOps
import random
import string
def createSquareWithLetter(name):
    letter = name[0]
    randRed = random.randint(0,255)
    randGreen = random.randint(0,255)
    randBlue = random.randint(0,255)
    background = Image.new('RGB', (128, 128), (randRed, randGreen, randBlue))
    square = ImageDraw.Draw(background)
    font = ImageFont.truetype("arial.ttf", 100)
    square.text((30, 18), letter , font = font)
    background.show()

createSquareWithLetter("Andy")
