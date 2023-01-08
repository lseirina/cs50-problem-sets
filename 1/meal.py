#get time from user
"""
def main():
    answer = input("What time is it now? ")
    time = convert(answer)
    if time >= 8 and time <= 9:
        print("breakfast time")
    if time >= 12 and time <= 13:
        print("lunch time")
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    hour,minut = time.split(":")
    minut_new = float(minut) / 60
    return float(hour) + minut_new

if __name__== main():
    main()
"""

def main():
    
    time = convert(input("What time is it? "))
    if 8 >= time >= 7:
        print("breakfast time")
    elif 13 >= time >= 12:
        print("lunch time")
    elif  19 >= time >= 18:
        print("dinner time")
    

def convert(time):
    hours,minutes = time.split(":")
    hours_new = float(hours)
    minutes_new = float(minutes)/60
    time_new = hours_new + minutes_new
    return time_new

if __name__ in "__main__":
    main()

