'''
Test this.
https://tritech-testsite.smapply.io/
Use your personal email.  Not your @ksd.org account.

python-circle-list-assignment.py
Get the code: 10.183.1.26 code python
Plot circle data using python
- Use your data
~ Change the background color
~ Change the graph line colors
~ Change the plot line color
~ Change the plot dot color
~ Label the graph with the text "Plotting Circumference and Diameter"
~ Label the axis with text (Circumference and Diameter)
~ Upload to github with your name initials or name attached (plot-circle-list-cwc.py)

'''

import turtle
import math
wdth = 800; hgth = 800


def grid(t):
	x = 0; y = 0
	t.color('white')
	while (x < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x,y+400)
		x = x + 50
	x = 0; y = 0
	while (y < 400):
		t.penup()
		t.goto(x,y)
		t.pendown()
		t.goto(x+400,y)
		y = y + 50
	t.penup()
	t.goto(-380,-250)
	t.pendown()
	t.color('springgreen')
	style = ('Courier', 30, 'bold')
	t.write('C i r c l e   C i r c u m f e r e n c e\n	a n d\n    D i a m e t e r   P l o t', font=("Comic Sans MS", 30, 'normal', 'bold',))
	t.color('deeppink')
	t.pu()
	t.goto(-30,0)
	t.write('C\ni\nr\nc\nu\nm\nf\ne\nr\ne\nn\nc\ne', font=("Comic Sans MS", 15, 'normal', 'bold',))
	t.pu()
	t.goto(0, -40)
	t.color('magenta')
	t.write('D i a m e t e r', font=("Comic Sans MS", 15, 'normal', 'bold',))
	t.hideturtle()
	t.penup()

def plotCircles(t):
	t.color('magenta')
	#list  named d and c
	d =  [8.3,9.8,4,7]
	c =  [26.1,30.8,12,22]
	# list dsorted and csorted
	dsorted = sorted (d, key = float)
	csorted = sorted(c , key = float)
	t.goto(0,0)
	t.pendown()

	t.goto(dsorted[0],csorted[0])
	t.dot(4, 'cyan')
	t.goto(dsorted[1],csorted[1])
	t.dot(4, 'cyan')
	t.goto(dsorted[2],csorted[2])
	t.dot(4, 'cyan')
	t.goto(dsorted[3],csorted[3])
	t.dot(4, 'cyan')

def main():
	try:
		turtle.tracer(0,0)
		turtle.TurtleScreen._RUNNING = True
		# get wdth and hgth globally
		turtle.screensize(canvwidth=wdth, canvheight=hgth, bg='black')
		#print(turtle.Screen().screensize())
		w = turtle.Screen()
		t = turtle.Turtle()

		t.hideturtle()
		grid(t)
		plotCircles(t)
		turtle.update()
		w.exitonclick()
	finally:
		turtle.Terminator()

if __name__ == '__main__':
	main()

'''
	# Using sorted + key
	Output = sorted(Input, key = float)
	# Using sorted + key
	Output = sorted(Input, key = float)
'''
