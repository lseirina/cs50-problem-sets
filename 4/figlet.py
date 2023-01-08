

from pyfiglet import Figlet
import sys
import random

 
figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False 
else:
    sys.exit("Invalid usage")


figlet.getFonts()
# m = input("Input: ")
if isRandomFont == False:
    try:
        figlet.setFont(font = sys.argv[2])
        
    except:
        print("Invalid usage")
        sys.exit(1)

else:
    font = random.choice(figlet.getFonts())
m = input("Input: ")
print("Output: ")
print(figlet.renderText(m))
"""




from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
item = input("Input: ")

if len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
elif len(sys.argv) > 2 and sys.argv[1] in ["-f", "-font"] and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid usage")    
print(f"Output: {figlet.renderText(item)}")

"""



