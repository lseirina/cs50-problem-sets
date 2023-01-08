from typing import List
"""

import inflect
import sys
p = inflect.engine()
list = []
while True:
    try:
        name = input("Name: ")
        if len(name) < 0:
            sys.exit(1)
        else:
            list.append(name)
    
           

    except EOFError:
           print()
           break

 
#mylist = p.join(("apple", "banana", "carrot"))
# print(mylist)

"""


import re
import inflect
p = inflect.engine()
#mylist = p.join(("apple", "banana", "carrot"))
# "apple, banana, and carrot"
list = []
while True:
    try:
        name = input("Name: ")
        if len(name) == 0:
            pass
        else:
            list.append(name)
    
    except  EOFError:
        print()
        break
        
mylist = p.join(list)
print(f"Adieu, adieu, to {mylist}")        