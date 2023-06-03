import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    string = input("Input: ")
    x = random.choice(fonts)
    figlet.setFont(font=x)
    print(figlet.renderText(string))
elif (len(sys.argv) == 3) and ((sys.argv[1] == '-f') or sys.argv[1] == '--font') and (sys.argv[2] in fonts):
    string = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(string))
elif (len(sys.argv) == 3) and ((sys.argv[1] != '-f') or sys.argv[1] != '--font') or (sys.argv[2] not in fonts):
    sys.exit("Invalid usage")


