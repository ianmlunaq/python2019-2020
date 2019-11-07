# triggeredTurtle.py | katona

import turtle

def arcR(t,x,y,l,tn,h):
	#x, y, l (length) tn(turn value)
	t.width(3)
	t.down()
	t.seth(h)
	for i in range (1,10):
			t.pencolor("black")
			t.forward(l)
			t.rt(tn)

def circle(t):
	print("circle")
	t.down()
	t.color("#ff0000")
	for i in range (0,10):
		t.forward(10)
		t.rt(36)

def circlefill(t,x,y,l):
	print("circle")
	t.penup()
	t.goto(x,y+r)
	t.down()
	t.begin_fill()
	t.color("#000000")
	for i in range (1,40):
		tn = 9
		if (i > 10 and i <20):
			tn = 5
		t.forward(l)
		t.rt(tn)
	t.end_fill()

def matrix():
	print("matrix")

def square(t,x,y):
	t.goto(x,y)
	t.penup()
	t.begin_fill()
	tcolor = "#0000ff"
	t.color(tcolor)
	t.forward(100)
	t.rt(90)
	t.forward(90)
	t.rt(90)
	t.forward(80)
	t.rt(90)
	t.forward(70)
	t.end_fill()

def turt():
	try:
		turtle.TurtleScreen._RUNNING = True
		turtle.screensize(canvwidth=700, canvheight=700, bg=None)
		x = -400; y = 0
		w = turtle.Screen()
		w.clear()
		w.bgcolor("#ffffff")
		t = turtle.Turtle()

		x = -400; y = 0
		t.speed(0)
		t.penup()

		t.goto(0,100)
		t.begin_fill()
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,11,90)
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,50,45,180)
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,11,0)
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,45,90)

		t.goto(260,-50)
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,45,90)
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,11,270)


		t.goto(145,-270)
		t.goto(140,-200)
		t.goto(135,-170)


		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,11,180)
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,45,270)

		t.goto(0,100)
		tcolor = "#00ff00";t.color(tcolor)
		arcR(t,x,y,25,45,270)
		t.end_fill()

		t.penup()
		t.right(130)
		t.forward(250)
		t.right(90)
		t.forward(100)
		t.color("red")
		t.pendown()
		t.begin_fill()
		t.forward(10)
		t.circle(10)
		t.end_fill()

		t.penup()
		t.forward(30)
		t.color("red")
		t.pendown()
		t.begin_fill()
		t.forward(10)
		t.circle(10)
		t.end_fill()
		w.exitonclick()
	finally:
		turtle.Terminator()

def main():
    turt()

if __name__ == '__main__':
	main()
