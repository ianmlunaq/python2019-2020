# turtleDriver.py | ian seth kat

import turtle
import rainbow
import olympicRings
import triggeredTurtle

def main():
	w = turtle.Screen()
	w.setup(1500, 1000)
	w.clear()
	w.bgcolor("#ffffff")
	w.title('A rainbow over the olympic rings next to a triggered turtle')
	t = turtle.Turtle()
	t.speed(0)

	rainbow.rainbow(t)
	print('\'rainbow.py\' Done!')
	olympicRings.rings(t)
	print('\'olympicRings.py\' Done!')
	triggeredTurtle.turt(t)
	print('\'triggeredTurtle.py\' Done!')


	w.exitonclick()




if __name__ == "__main__":
	main()
