"""
import re
import sys


def main():
    print(convert(input("Hours: ")))

# Hours: 9:00 AM to 5:00 PM                                                       
# 09:00 to 17:00                                                                                                                           
# Hours: 9 AM to 5 PM                                                             
# 09:00 to 17:00                                                                                                                               
# Hours: 9 AM to 5:30 PM                                                     
# 09:00 to 17:30    
# 22:30 to 08:50

def convert(s):
    matches = re.search("^([1-9]|1[0-2])(\:[0-5][0-9])? ([AP]M) to ([1-9]|1[0-2])(\:[0-5][0-9])? ([AP]M)",s)
    if matches:
        pieces = matches.groups()
        if int(pieces[0]) > 12 and int(pieces[3]) > 12:
            raise ValueError

        first_time = format_convert(pieces[0],pieces[1],pieces[2])
        second_time = format_convert(pieces[3],pieces[4],pieces[5])
    else:
        raise ValueError
    return f"{first_time} to {second_time}"

def format_convert(hour,minutes,pm_am):
    if pm_am == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
            
    else:
        if int(hour) == 12:
            new_hour = 0
        else:
            new_hour = int(hour)
    if minutes == None:
        new_minutes = ":00"
        new_time =f"{new_hour:02}" + new_minutes
    else:
        new_time = f"{new_hour:02}" + minutes
    return new_time
"""


import re
import sys

# Hours: 9:00 AM to 5:00 PM                                                       
# 09:00 to 17:00                                                                                                                           
# Hours: 9 AM to 5 PM                                                             
# 09:00 to 17:00                                                                                                                               
# Hours: 9 AM to 5:30 PM                                                     
# 09:00 to 17:30  
# 10:30 PM to 8:50 AM
# 22:30 to 08:50
# 12:00 AM to 5:00 PM
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
        matches = re.search(r"^([1-9]|1[0-2])(\:[0-5][0-9])? ([A,P]M) to ([1-9]|1[0-2])(\:[0-5][0-9])? ([A,P]M)$", s)
        if matches:
            first_time = convert_time(matches.group(1),matches.group(2),matches.group(3))
            last_time = convert_time(matches.group(4),matches.group(5),matches.group(6))
            return f"{first_time} to {last_time}"
        else: 
            raise ValueError

def convert_time(hour, minutes, am_pm):
   
    if am_pm == "AM":
        if hour == "12":
            hour_new = 00
        else:
            hour_new = int(hour) 
        
    else:
        if hour == "12":
            hour_new = 12
        else:
            hour_new = int(hour) + 12
    
    if minutes == None:
        minutes_new = ":00"
    else:
        minutes_new = minutes

    time_new = f"{hour_new:02}{minutes_new}"
    return time_new

if __name__ == "__main__":
    main()
















# def convert(s):
    
#         matches = re.search(r"^([1-9]|1[0-2])(\:[0-5][0-9])? ([AP]M) to ([1-9]|1[0-2])(\:[0-5][0-9])? ([AP]M)$", s)

#         if matches:
#                 # if matches.group(2) == None:
#                 #     return matches.group(2) == "00"
#                 # if matches.group(5) == None:
#                 #     return matches.group(5) == "00"   
#                 if matches.group(3) == "PM":
#                     hour1 = int(matches.group(1)) + 12
#                     return(f"{hour1}{matches.group(2)} to 0{matches.group(4)}{matches.group(5)}")
#                 if matches.group(6) == "PM":
#                     hour2 = int(matches.group(4)) + 12         
#                     return(f"0{matches.group(1)}{matches.group(2)} to {hour2}{matches.group(5)}")
#         else:
#                 raise ValueError
        
        
                # if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
                #     raise ValueError
                # if int(matches.group(2)) >= 60 or int(matches.group(5)) >= 60:
                #     raise ValueError
                    
            
        
            
if __name__ == "__main__":
    main()