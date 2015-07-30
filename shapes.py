'''
These are just stupid shapes I was trying to make...
if you run it you'll see. there's like a bunch of these problems on websites.
'''


def thing():
    num = 0
    space = ' '
    length = 0
    val = '@'
    for i in range(10):
        num += 1
        print((val*num)+(space*(18-length))+(val*num))
        length += 2

def thing2():
    space = ' '
    length = 0
    val = '$'
    num = 1
    LENGTH = 1
    NUM = 7
    for i in range(10):
        if i < 5:
            print (space*(4-length)+ (val*num) + (space*(4-length)))
            num +=2
            length +=1
        if i > 5:
            print ((space*LENGTH)+(val*NUM)+(space*LENGTH))
            NUM -= 2
            LENGTH+=1

def thing3():
    space = ' '
    length = 7
    val = '#'
    LENGTH = 1
    LEN = 0
    LENG = 3
    for i in range (10):
        if i < 4 :
            print ((space *LEN)+ val + (space*length) + val + (space*LEN))
            LEN += 1
            length -= 2
        if i > 5:
            print ((space * LENG) + val + (space * LENGTH) + val + (space * LENG))
            LENGTH += 2
            LENG -=1
        if i == 5:
            print ((space*4)+ val + (space*4))
    
        

thing()
thing2()
thing3()
