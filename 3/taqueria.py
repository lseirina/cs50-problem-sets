
from ast import While

"""
manu = {"Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00}
total_amount = 0
while True:
    try:
        item = input("Item: ").title()
        if item in manu:
            total_amount += manu[item]
            print("Total: $", end = "")
            print("{:.2f}".format(total_amount))
            
    except EOFError:
        break
    

              
#total = manu[item] + manu[item]
"""


menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    
    try:
        item = input("Item: ").title()
        if item in menu:
            total += menu[item]
            total_doller = "Total: ${:.2f}"
            print(total_doller.format(total))
       
        
    except EOFError:
       break

