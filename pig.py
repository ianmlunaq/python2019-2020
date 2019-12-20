# pig.py | iml

import random

p1PointsTemp = 0
p1PointsPerm = 0

while p1PointsPerm < 100:
    roll = random.randint(1,6)
    print(roll)
    decision = input('')
    if roll == 1:
        p1PointsPerm += 0
    else:
        p1PointsPerm += roll

    print('total: ' + str(p1PointsPerm))
    decision = input('')


print(str(p1PointsPerm))
