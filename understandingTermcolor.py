from termcolor import colored, cprint

text = colored('Hello, World!', 'white', 'on_blue', attrs=['reverse', 'blink'])
print(text)

cprint('Hello, World!', 'white', 'on_blue')

"""
Text colors:
    grey
    red
    green
    yellow
    blue
    magenta
    cyan
    white

Text highlights:
    on_grey
    on_red
    on_green
    on_yellow
    on_blue
    on_magenta
    on_cyan
    on_white

Attributes:
    bold
    dark
    underline
    blink
    reverse
    concealed
"""
