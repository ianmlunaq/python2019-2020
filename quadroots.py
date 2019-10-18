#quadroots.py | CWC | Reference: Amit Saha(Doing Math with Python)

def roots(a,b,c):
	D = (b*b - 4*a*c)
	print()
	print("D = " + str(D))
	if(D >= 0):
		print("REAL ROOTS")
		D = D**0.5
		x1 = (-b + D) / (2*a)
		x1 = (-b - D) / (2*a)
		print("x1 = " + str(x1) + " x2 = " + str(x2))
		
	elif(D < 0):
		D = (D * -1)**0.5;
		print("IMAGINARY ROOTS")
		print("x1 = -" + str(b/(2*a)) + " - " +str(D/(2*a)) + "i")
		print("x1 = -" + str(b/(2*a)) + " + " +str(D/(2*a)) + "i")

_name_ = "_main_"

if _name_ == '_main_':
	print("Input a, b, and c for the quadratic (ax^2 + bx +c)")
	a = input("Enter a: ")
	b = input("Enter b: ")
	c = input("Enter c: ")
	roots(float(a), float(b), float(c))

"""
Output:

Input a, b, and c for the quadratic (ax^2 + bx +c)
Enter a: 1
Enter b: 0
Enter c: 9

D = -36.0
IMAGINARY ROOTS
x1 = -0.0 - 3.0i
x1 = -0.0 + 3.0i

"""
