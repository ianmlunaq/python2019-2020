#battleship.py | ian luna
from colorama import Fore, Back, Style
from termcolor import colored, cprint

# Using above first method to create a
# 2D array
rows, cols = (5, 5)
arr = [[0]*cols]*rows
print(arr)

for row in arr:
    db = row % 2
    print(db)
