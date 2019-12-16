# 65536Letters.py | iml

import random
import datetime

f = ''
filename = ''

def randoLetters():
    global f
    for x in range(65536):
        y = random.randint(65,90)
        c = chr(y)
        f += c
        #print(c,end='')

def fileName():
    global filename
    x = datetime.datetime.now()
    filename = str(x.year) + str(x.month) + str(x.day) + '-' + str(x.hour) + str(x.minute) + str(x.second) + '.txt'
    #nowString = filename

randoLetters()
print(f)


# The following is to output to a file
"""
fileName()

file = open(filename, 'w')
file.write(f)
file.close()
"""
