"""

def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)


def convert(fraction):

    while True:
        try:
            x,y = fraction.split("/")   
            new_x = int(x)
            new_y = int(y)      
            fraction_new = new_x / new_y
            if fraction_new <= 1:
                p = int(fraction_new * 100)
                return p
            else: 
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise
        
    
def gauge(percentage):
    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    else:
        return str(percentage) + "%"
    

if __name__=="__main__":
    main()

"""


"""
while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x_new = int(x)
        y_new = int(y)
        result = x_new / y_new
        if result <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
    
p = round(result * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
"""

def main():
    fraction = input("Fraction: ")
    output = gauge(convert(fraction))
    print(output)

def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            x_new = int(x)
            y_new = int(y)
            result = x_new / y_new
            if result <= 1:
                break
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
           raise
    percentage = round(result * 100)
    return percentage
def gauge(percentage):
    if percentage <= 1:
        return  "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"
    


if __name__ == "__main__":
    main()
