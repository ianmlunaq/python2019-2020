import turtle

def blackring(t):
	t.home()
	t.seth(0)
	t.down()
	t.color("#000000")
	t.width(12)
	for i in range (1,50):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))


def bluering(t):
	t.goto(-160,0)
	t.seth(0)
	t.down()
	t.color("#1e90ff")
	t.width(12)
	for i in range (1,50):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))


def redring(t):
	t.goto(160,0)
	t.seth(0)
	t.down()
	t.color("#e8434c")
	t.width(12)
	for i in range (1,50):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))


def yellowring(t):
	t.goto(-80,-66)
	t.seth(0)
	t.down()
	t.color("#ffd700")
	t.width(12)
	for i in range (1,50):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))


def greenring(t):
	t.goto(80,-66)
	t.seth(0)
	t.down()
	t.color("#2e8b57")
	t.width(12)
	for i in range (1,50):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))
def circle(t):
	t.down()
	t.color("#ff0000")
	for i in range (1,20):
		t.forward(10)
		t.rt(18)
	t.color("#ffffff")


def main():
	x = -30; y = 0
	w = turtle.Screen()
	w.setup(1000, 700)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	t.hideturtle()
	t.penup()
	t.goto(0,0)
	t.speed(10)
	t.color("#000000")
	blackring(t)
	t.up()
	bluering(t)
	t.up()
	redring(t)
	t.up()
	yellowring(t)
	t.up()
	greenring(t)

	w.exitonclick()


if __name__ == '__main__':
	main()

'''
#apt install python3-tk



wn = turtle.Screen()   # create a turtle
t = turtle.Turtle()
t.color('green')      # set the color
t.forward(50)         # draw a green line of leng
t.up()                # lift up the tail
t.forward(50)         # move forward 50 without drawing
t.right(90)           # change direction to the right, left works too
t.down()              # put the tail down
t.backward(100)       # draw a green line 100 units long
wn.exitonclick()
'''
