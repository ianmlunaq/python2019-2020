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
        """
        while decision != 'h' or decision != 'hold' or decision != 'c':
            if decision == 'help':
                print('Pig is a simple dice game first described in print by John Scarne in 1945. As with many games of folk origin, Pig is played with many rule variations.')
                print('In this version of Pig, each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to "hold": ')
                print('     If the player rolls a 1, they score nothing and it becomes the next player\'s turn.')
                print('     If the player rolls any other number, it is added to their turn total and the player\'s turn continues.')
                print('     If a player chooses to \"hold\", their turn total is added to their score, and it becomes the next player\'s turn.')
                print('The first player to score 100 or more points wins.')
                print('For example, the first player, Donald, begins a turn with a roll of 5. Donald could hold and score 5 points, but chooses to roll again. Donald rolls a 2, and could hold with a turn total of 7 points, but chooses to roll again. Donald rolls a 1, and must end his turn without scoring. The next player, Alexis, rolls the sequence 4-5-3-5-5, after which she chooses to hold, and adds her turn total of 22 points to her score.')

            print('If you need help type \"help\".')
            print()
            decision = input('Do you want to continue or hold? ')
        """
        if decision == 'h' or 'hold':
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
