# turtledriver.py | ian seth kat

import turtle
import rainbow
import olympicrings
import kat

def main():
	w = turtle.Screen()
	w.setup(1500, 1000)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	t.speed(0)

	rainbow.rainbow(t)
	olympicrings.rings(t)
	kat.turt(t)

	w.exitonclick()




if __name__ == "__main__":
	main()
