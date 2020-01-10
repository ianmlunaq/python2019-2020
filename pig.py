# pig.py | iml

import random

p1PointsTemp = 0
p1PointsPerm = 0

p2PointsTemp = 0
p2PointsPerm = 0

win = 0
pc = 0

print()

while win == 0:
    while pc == 0:
        pc = 0
        roll = random.randint(1,6)
        print('P1 ' + str(roll))

        if roll == 1:
            p1PointsTemp = 0
            pc = 1
            print('You got a 1!')
            print()
            confirmation = input()
            break;
        else:
            p1PointsTemp += roll

        print('TempPoints: ' + str(p1PointsTemp))
        print('PermPoints: ' + str(p1PointsPerm))
        decision = input('Do you want to continue or hold? ')
        print()
        if decision == 'h':
            p1PointsPerm += p1PointsTemp
            p1PointsTemp = 0
            pc = 1
        if p1PointsPerm >= 100:
            win += 1

    while pc == 1:
        pc = 1
        roll = random.randint(1,6)
        print('PC ' + str(roll))

        if roll == 1:
            p2PointsTemp = 0
            pc = 0
            print('You got a 1!')
            print()
            confirmation = input()
            break;
        else:
            p2PointsTemp += roll

        print('TempPoints: ' + str(p2PointsTemp))
        print('PermPoints: ' + str(p2PointsPerm))
        confirmation = input()
