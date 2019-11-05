import turtle

def blackring(t):
	t.home()
	t.seth(0)
	t.down()
	t.color("#000000")
	t.width(12)
	for i in range (1,42):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))

def blackringfill1(t):
	t.goto(8,0)
	t.seth(180)
	t.color('#000000')
	t.down()
	for i in range (1,4):
		t.fd(10)
		t.rt(9)
		print(str(t.pos()))

def blackringfill2(t):
	t.goto(68,61)
	t.seth(90)
	t.color("#000000")
	t.down()
	for i in range (1,2):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))
	t.up()
	t.goto(68,61)
	t.seth(270)
	t.down()
	for i in range (1,2):
		t.fd(10)
		t.rt(9)
		print(str(t.pos()))

def bluering(t):
	t.goto(-160,0)
	t.seth(0)
	t.down()
	t.color("#1e90ff")
	t.width(12)
	for i in range (1,42):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))

def blueringfill(t):
	t.color('#ff00ff')
	t.goto(-91,61)
	t.seth(90)
	t.color("#1e90ff")
	t.down()
	for i in range (1,2):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))
	t.up()
	t.goto(-91,61)
	t.seth(270)
	t.down()
	for i in range (1,2):
		t.fd(10)
		t.rt(9)
		print(str(t.pos()))

def redring(t):
	t.goto(160,0)
	t.seth(0)
	t.down()
	t.color("#e8434c")
	t.width(12)
	for i in range (1,42):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))

def redringfill(t):
	t.goto(168,0)
	t.seth(180)
	t.color("#e8434c")
	t.down()
	for i in range (1,4):
		t.fd(10)
		t.rt(9)
		print(str(t.pos()))

def yellowring(t):
	t.goto(-80,-66)
	t.seth(0)
	t.down()
	t.color("#ffd700")
	t.width(12)
	for i in range (1,42):
		t.fd(10)
		t.lt(9)
		print(str(t.pos()))

def greenring(t):
	t.goto(80,-66)
	t.seth(0)
	t.down()
	t.color("#2e8b57")
	t.width(12)
	for i in range (1,42):
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


def rings(t):
	t.shape('classic')
	#t.hideturtle()
	t.penup()
	t.shape('classic')
	#t.hideturtle()
	t.penup()
	t.goto(0,0)
	t.speed(0)
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
	t.up()
	blueringfill(t)
	t.up()
	blackringfill1(t)
	t.up()
	blackringfill2(t)
	t.color('#ff00ff')
	t.up()
	redringfill(t)
	t.hideturtle()


def main():
	x = -30; y = 0
	w = turtle.Screen()
	w.setup(1000, 700)
	w.clear()
	w.bgcolor("#ffffff")
	t = turtle.Turtle()
	rings(t)
	w.exitonclick()


if __name__ == '__main__':
	main()
