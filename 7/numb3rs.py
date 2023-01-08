import re
import sys
# def main():
#     try:
#         print(validate(input("IPv4 Address: ")))
#     except:
#         sys.exit("False")


# def validate(ip):
#     matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$",ip)
#     number1 = int(matches.group(1))
#     number2 = int(matches.group(2))
#     number3 = int(matches.group(3))
#     number4 = int(matches.group(4))
    
#     if matches and  0 <= number1 <= 255 and  0 <= number2 <= 255 and  0 <= number3 <= 255 and  0 <= number4 <= 255:
#         return True
#     else:
#         return False
    
# if __name__ =="__main__":
#     main()
"""
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        matches_numbers = ip.split(".")
        for num in matches_numbers:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
    """



import re
import sys

#255.255.255.0

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        match = re.search(r"^([1-2]?[0-5]?[0-9])\.([1-2]?[0-5]?[0-9])\.([1-2]?[0-5]?[0-9])\.([1-2]?[0-5]?[0-9])$", ip)
        if int(match.group(1)) > 255 or int(match.group(2)) > 255 or int(match.group(3)) > 255 or int(match.group(4)) > 255:
            return False
    except:
        return False
    return True

if __name__ == "__main__":
    main()