# rainbow.py | seth

import turtle

def arcR(t,x,y,l,tn,h):
	#x, y, l (length) tn(turn value)
	t.down()
	t.seth(h)
	for i in range (1,10):
			t.forward(l)
			t.rt(tn)

def circle(t):
	print("circle")
	t.down()
	t.color("#ff0000")
	for i in range (0,10):
		t.forward(10)
		t.rt(36)

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

def rainbow(t):
	x = -400; y = 0
	t.speed(0)
	t.penup()
	t.goto(-700,50)
	t.pendown()
	t.begin_fill()
	tcolor = "#ff0000";t.color(tcolor)
	arcR(t,x,y,75,11.25,90)
	tcolor = "#ff0000";t.color(tcolor)
	arcR(t,x,y,75,11.25,0)
	t.end_fill()

	t.penup()
	t.begin_fill()
	t.goto(-645,50)
	tcolor = "#ffa500";t.color(tcolor)
	arcR(t,x,y,65,11.25,90)
	tcolor = "#ffa500";t.color(tcolor)
	arcR(t,x,y,65,11.25,0)
	t.end_fill()

	t.penup()
	t.begin_fill()
	t.goto(-585,50)
	tcolor = "#ffff00";t.color(tcolor)
	arcR(t,x,y,55,11.25,90)
	tcolor = "#ffff00";t.color(tcolor)
	arcR(t,x,y,55,11.25,0)
	t.end_fill()

	t.penup()
	t.begin_fill()
	t.goto(-525,50)
	tcolor = "#008000";t.color(tcolor)
	arcR(t,x,y,45,11.25,90)
	tcolor = "#008000";t.color(tcolor)
	arcR(t,x,y,45,11.25,0)
	t.end_fill()

	t.penup()
	t.begin_fill()
	t.goto(-465,50)
	tcolor = "#0000ff";t.color(tcolor)
	arcR(t,x,y,35,11.25,90)
	tcolor = "#0000ff";t.color(tcolor)
	arcR(t,x,y,35,11.25,0)
	t.end_fill()

	t.penup()
	t.begin_fill()
	t.goto(-405,50)
	tcolor = "#4b0082";t.color(tcolor)
	arcR(t,x,y,25,11.25,90)
	tcolor = "#4b0082";t.color(tcolor)
	arcR(t,x,y,25,11.25,0)
	t.end_fill()

	t.penup()
	t.begin_fill()
	t.goto(-345,50)
	tcolor = "#8a2be2";t.color(tcolor)
	arcR(t,x,y,15,11.25,90)
	tcolor = "#8a2be2";t.color(tcolor)
	arcR(t,x,y,15,11.25,0)
	t.end_fill()

	t.penup()
	t.begin_fill()
	t.goto(-285,50)
	tcolor = "#ffffff";t.color(tcolor)
	arcR(t,x,y,5,11.25,90)
	tcolor = "#ffffff";t.color(tcolor)
	arcR(t,x,y,5,11.25,0)
	t.end_fill()

	t.hideturtle()

def rainbowv2():
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

		t.goto(-400,-100)
		t.pendown()
		t.begin_fill()
		tcolor = "#ff0000";t.color(tcolor)
		arcR(t,x,y,75,11.25,90)
		tcolor = "#ff0000";t.color(tcolor)
		arcR(t,x,y,75,11.25,0)
		t.end_fill()
		t.penup()
		t.begin_fill()

		t.goto(-345,-100)
		tcolor = "#ffa500";t.color(tcolor)
		arcR(t,x,y,65,11.25,90)
		tcolor = "#ffa500";t.color(tcolor)
		arcR(t,x,y,65,11.25,0)
		t.end_fill()
		t.penup()
		t.begin_fill()

		t.goto(-285,-100)
		tcolor = "#ffff00";t.color(tcolor)
		arcR(t,x,y,55,11.25,90)
		tcolor = "#ffff00";t.color(tcolor)
		arcR(t,x,y,55,11.25,0)
		t.end_fill()
		t.penup()
		t.begin_fill()

		t.goto(-225,-100)
		tcolor = "#008000";t.color(tcolor)
		arcR(t,x,y,45,11.25,90)
		tcolor = "#008000";t.color(tcolor)
		arcR(t,x,y,45,11.25,0)
		t.end_fill()
		t.penup()
		t.begin_fill()

		t.goto(-165,-100)
		tcolor = "#0000ff";t.color(tcolor)
		arcR(t,x,y,35,11.25,90)
		tcolor = "#0000ff";t.color(tcolor)
		arcR(t,x,y,35,11.25,0)
		t.end_fill()
		t.penup()
		t.begin_fill()

		t.goto(-105,-100)
		tcolor = "#4b0082";t.color(tcolor)
		arcR(t,x,y,25,11.25,90)
		tcolor = "#4b0082";t.color(tcolor)
		arcR(t,x,y,25,11.25,0)
		t.end_fill()
		t.penup()
		t.begin_fill()

		t.goto(-45,-100)
		tcolor = "#8a2be2";t.color(tcolor)
		arcR(t,x,y,15,11.25,90)
		tcolor = "#8a2be2";t.color(tcolor)
		arcR(t,x,y,15,11.25,0)
		t.end_fill()
		t.penup()
		t.begin_fill()

		t.goto(15,-100)
		tcolor = "#ffffff";t.color(tcolor)
		arcR(t,x,y,5,11.25,90)
		tcolor = "#ffffff";t.color(tcolor)
		arcR(t,x,y,5,11.25,0)
		t.end_fill()

		t.hideturtle()
		w.exitonclick()
	finally:
		turtle.Terminator()

def main():
	rainbowv2()

if __name__ == '__main__':
	main()
