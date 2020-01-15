import math
n = float(input("Input a decimal greater than 1 : "))
ni = int(n)
nd = n % ni
nd = (math.fabs(nd))
print(nd)
