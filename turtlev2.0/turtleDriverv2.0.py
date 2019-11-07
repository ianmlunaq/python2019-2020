# turtleDriverv2.0.py | ian seth kat

import turtle
import rainbow
import olympicRings
import evilTurtle

def main():
    done = 0
    q = input('Turtle, rainbow, or olympic rings? (\'s\' to stop) ')
    q = q.lower()

    if (q == 's' or q == 'stop'):
        done = 1
    while (done == 0):
        if(q == 't' or q == 'turtle'):
            evilTurtle.main()
        elif(q == 'r' or q == 'rainbow'):
            rainbow.main()
        elif(q == 'o' or q == 'olympicrings' or q == 'olympic rings' or q == 'rings' or q == 'or'):
            olympicRings.main()

        q = input('Turtle, rainbow, or olympic rings? (\'s\' to stop) ')
        if (q == 's' or q == 'stop'):
            done = 1

if __name__ == '__main__':
    main()
