# basecon.py iml
def bincon(num, addSpace):
	n = num
	s = addSpace
	#print(n,s)	#debug
	print(n, " = ", end = "")
	d = 128
	binString = ""            #create a stirng called binString

	for i in range(0, 8):
		q = int(n / d)
		r = int(n % d)
		n = r
		d = int(d / 2)
		binString = binString + str(q)
		
		if i == 3 and s == 1:
			binString += " "
			
	print(binString)
	
def main():
	bincon(152, 1)
	bincon(191, 0)
	bincon(7, 1)
	
main()
