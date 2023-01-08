"""
mounths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        mounth,day,year = date.split("/")
        if (int(day)  >= 1 and int(day) <= 31) and (int(mounth) >= 1 and int(mounth) <= 12):
            break
    except:
        try:
            mounth_old, day_old, year = date.split(" ")
            for i in range(len(mounths)):
                if mounth_old == mounths[i]:
                    mounth = i + 1
            day = day_old.replace(",","")
            if (int(day)  >= 1 and int(day) <= 31) and (int(mounth) >= 1 and int(mounth) <= 12):
                break
                
        except:
            print()
            pass

print(f'{year}-{int(mounth):02}-{int(day):02}')

"""

monthes = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Date: 8/9/1636                                                                  
# 1636-08-09  

# Date: January 1, 1970                                                           
# 1970-01-01 
import re
while True:
    try:
        date = input("Date: ").strip()
        if matches:= re.search(r'^(\" )?[0-9][0-9]?\/[0-9][0-9]?\/[0-9]{4}(\ ")?$', date):
            month, day, year = date.split("/")
            # month_new = month.replace(' ', '')
            #year_new = year.replace(' ', '')
            if 0 < int(day) <= 31 and 0 < int(month) <= 12:
                print(f"{year}-{int(month):02}-{int(day):02}")
                break
            else:
                pass
        else:
            month_1, day_1, year_1 = date.split(" ")
            if "," in day_1:
                day_2 = day_1.replace(",","")
            else:
                input("Date: ")
            
            if month_1 in monthes and 31 >= int(day_2) > 0:
                month_2 = monthes.index(month_1) + 1
                print(f"{year_1}-{int(month_2):02}-{int(day_2):02}")
                break
            else:
                pass
          

    except ValueError:
        pass



