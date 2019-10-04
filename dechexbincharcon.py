# dechexbincharcon.py iml

thenumber = int(input("Input a whole, positive number: "))

def hexcon(num):
	h16s = ""; h1s = ""; hexLetter = ""
	h16 = num // 16
	h1 = int(num % 16)
	
	if h1 > 9:
		hexLetter = str(chr(87 + h1))
		h1 = ""
		
	h16s = str(h16); h1s = str(h1)
	h = h16s + h1s + hexLetter
	return h
	
def bincon(num):
	n = num
	#print(n)	#debug
	#print(n, " = ", end = "") 
	d = 128
	binString = ""            #create a string called binString

	for i in range(0, 8):
		q = int(n / d)
		r = int(n % d)
		n = r
		d = int(d / 2)
		binString = binString + str(q)
		
		if i == 3:
			binString += " "
			
	return binString
	
char = chr(thenumber)
print(char)
	
def main():
	dec = str(thenumber)
	hex = hexcon(thenumber)
	bin = bincon(thenumber)
	
	print(dec, hex, bin)
	
main()

