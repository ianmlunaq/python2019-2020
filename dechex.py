# dechex2.py iml

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
	
def main():
	hs = ""; hs2 = ""
	hs = hexcon(147); hs2 = hexcon(128)
	print(hs, hs2)	#debug

main()
