'''
Kristin Moser
CS1122 HW 10
km3322
encoding and decoding
'''
from __future__ import print_function
import urllib
import hashlib
#Decimal Encode
def encodeDec(string):
    for char in string:
        print (ord(char), end=' ')
    print()
#Decimal Decode
def decodeDec(string):
    nums = string.split()
    for num in nums:
        num = int(num)
        print (chr(num), end='')
    print()

#Decimal to Hexidecimal
def decToHex(string):
    print (hex(int(string)))
    
#Hexidecimal to Decimal
def hexToDec(string):
    print (int(string, 0))

#Decimal to Binary
def decToBin(string):
    print (bin(int(string)))
#Binary to Hexadecimal
def binToHex(string):
    print (hex(int(string)))

#Base 64 encode
def sixtyFourEncode(string):
    print (string.encode('base64','strict'))
#Base 64 decode
def sixtyFourDecode(string):
    print (string.decode('base64','strict'))

#URL encode
def URLencode(string):    
    print (urllib.quote(string))
#URL decode
def URLdecode(string):
    print (urllib.unquote(string))
#Hash with MD5
def aHashFUNC(string):
    print( hashlib.md5(string).digest())

#Hash with SHA-1
def anothaHashFUNC(string):
    print (hashlib.sha1(string).digest())

encodeDec("Chemistry is an odd class for CS majors to take" )
decodeDec("80 104 121 115 105 99 115 32 105 115 32 119 101 105 114 100 32 116 111 111")
decToHex("235")
hexToDec("0xbe")
decToBin("1400")
binToHex("10100111001")
sixtyFourEncode("Use the .encode() method")
sixtyFourDecode("SSBob3BlIHlvdSB1c2VkIHRoZSBkZWNvZGUgbWV0aG9k")
URLencode("The pasta & the sauce are tasty")
URLdecode("Wall-E%20%26%20Eve%20are%20totally%20the%20best%20Disney%20characters")
aHashFUNC("magical blubber cats")    
anothaHashFUNC("magical blubber cats")  
