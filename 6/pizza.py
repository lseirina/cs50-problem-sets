"""

import sys
from tabulate import tabulate
import csv
def main():
    check_command_line()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
        
            print(tabulate(reader, headers = "keys", tablefmt = "grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")
def check_command_line():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if not ".csv" in sys.argv[1]:
        sys.exit("Not a CSV file")



if __name__== "__main__":
    main()

    """



import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments") 

try:
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        #headers = ["item", "qty"]
        #headers = ["Sicilian Pizza", "Small", "Large"]
        
        print(tabulate(reader, headers = "keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")