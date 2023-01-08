"""
import re
import sys
def main():
    print(count(input("Text: ")))
# Um, thanks, um...
#um, hello, um, world
def count(s):
    
    um_list = re.findall(r"\,?\bum\,?", s, re.IGNORECASE)
    return len(um_list)


if __name__ in "__main__":
    main()
"""



import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"(?:[a-z])?\b(um)\b(?: [a-z]*)?", s, re.IGNORECASE)
    if matches:
        return len(matches)
    else:
        return 0

if __name__ == "__main__":
    main()