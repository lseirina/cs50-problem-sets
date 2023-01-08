
"""
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("valid")

    else:
        print("invalid")


def is_valid(s):

    if s[0].isalpha() == False or s[1].isalpha() == False:
            return False

    if len(s) > 6 or len(s) < 2:
            return False

    if s.isupper() == False:
            return False
    
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False  
            else:
                break
 
        i = i + 1
        
    for c in s:    
        
        if c in [",", ".", "!", " ", "?"]:
            return False
    return True


if __name__ == "__main__":
    main()
    

"""



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if  len(s) > 6 or len(s)< 2:
        return False
    if s.isupper() == False:
        return False
    if s[:1].isalpha() == False:
        return False
    for c in s:
        if c in [",",".","?","!", " "]:
            return False
    for i in range(len(s)):
        if s[i].isdigit():
            if not s[i:].isdigit():
                return False
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i += 1
    return True

if __name__=="__main__":
    main()
