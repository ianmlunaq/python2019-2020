# chatbot.py | iml

from array import *
import random

def randoChar():
    num = random.randint(33,126)
    char = chr(num)
    return char

a1 = randoChar()
a2 = randoChar()
a3 = randoChar()
a4 = randoChar()

b1 = randoChar()
b2 = randoChar()
b3 = randoChar()
b4 = randoChar()

c1 = randoChar()
c2 = randoChar()
c3 = randoChar()
c4 = randoChar()

d1 = randoChar()
d2 = randoChar()
d3 = randoChar()
d4 = randoChar()

grid = [[a1, a2, a3, a4], [b1, b2, b3, b4], [c1, c2, c3, c4], [d1, d2, d3, d4]]

"""
print(grid[0])
print(grid[1])
print(grid[2])
print(grid[3])

print(grid[0][0])
"""

for r in grid:
    for c in r:
        print(c,end = " ")
    print()
print()

#item = random.choice(grid)
#print(str(grid[0][3]))
num = 0

for x in range(5):
    randoCol = random.randint(0,3)
    randoRow = random.randint(0,3)

    botCheck = input("What is the character at " + str(randoCol+1) + ', ' + str(randoRow+1) + '? ')
    #print(str(grid[randoRow][randoCol])) #debug

    if botCheck != grid[randoRow][randoCol]:
        num += 1


if num > 0:
    print()
    print('TEST FAILED')
else:
    print()
    print('TEST PASSED')
