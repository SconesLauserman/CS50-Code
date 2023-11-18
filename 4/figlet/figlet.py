from pyfiglet import Figlet
import sys
import random

the_font = ""
figlet = Figlet()

if len(sys.argv) > 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            the_font = sys.argv[2]
        else:
            sys.exit(1)
    else:
        sys.exit(1)
else:
    sys.exit(1)
figlet.setFont(font=the_font)
user = input("Input: ")
print("Output: \n", figlet.renderText(user))
