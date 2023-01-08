"""
from curses.ascii import isspace
import sys

def main():
    check_command_line_argv()

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count_line = 0
    for line in lines:
        if check_comment_and_blank_lines(line) == False:
            count_line += 1
    print(count_line)

def check_command_line_argv():
    if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
            sys.exit("Not a Python file")



def check_comment_and_blank_lines(line): 
    if line.lstrip().startswith("#"):
        return True
    if line.isspace():
        return True
    return False
       

        
if __name__=="__main__":
    main()

    """



import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".py") == False:
    sys.exit("Not a Python file")
try:
    with open(sys.argv[1]) as file:
        count = 0
        for line in file:
            if line.lstrip().startswith("#") == False and line.isspace() == False:
                count += 1
    print(count)
except FileNotFoundError:
    sys.exit("File does not exist")


