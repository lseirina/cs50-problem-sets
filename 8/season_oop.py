"""

from ast import operator
from datetime import date
import sys
import inflect
import operator
import re

# def main():


#     today = str(date.today())
#     year,month,day = today.split("-")
#     date_of_birth = validate(input("Date of Birth: "))
#     year_birth,month_birth,day_birth = date_of_birth.split("-")
#     year_dif = operator.sub(int(year),int(year_birth))
#     month_dif = abs(operator.sub(int(month),int(month_birth)))
#     day_dif = abs(operator.sub(int(day),int(day_birth)))
#     year_in_minutes = year_dif * 365 * 24 * 60
#     month_in_minutes = month_dif * 30 * 24 * 60
#     day_in_minutes = day_dif * 24 * 60
#     total = year_in_minutes + month_in_minutes + day_in_minutes
#     inflector = inflect.engine()
#     words = inflector.number_to_words(total)
#     words_no_and = words.replace(" and","")
#     print(f"{words_no_and} minutes")


# def validate(n):
#         matches = re.search(r"^[0-9]{4}\-[0-1][0-9]\-[0-3][0-9]$", n)
#         if matches:
#             return n
#         else:
#             sys.exit("Invalid date")
    
# if __name__ in "__main__":
#     main()

p = inflect.engine()

class Born:
    def __init__(self, date_birth):
        self.date_birth = date_birth

    @classmethod
    def get_birthday(cls):
        birthday = input("Date of birth: ")
        check = birthday
        if check := re.search(r"^([0-9]{4})\-([0-9]{2})\-([0-9]{2})$", check):
            year = int(check.group(1))
            month = int(check.group(2))
            day = int(check.group(3))
            birth = date(year, month, day)
            return birth
        else:
            sys.exit("Invalid date")
        
class Today:
    def __init__(self, today):
        self.today = today

    @classmethod
    def get_today(cls):
        today = date.today()
        return today

def main():
    born = Born.get_birthday()
    today = Today.get_today()
    dif = today - born
    dif = dif.days
    minutes = dif * 24 * 60
    words = p.number_to_words(minutes, andword = "")
    print(f"{words} minutes")

if __name__ in "__main__":
    main()





# def main():
#     date_of_birth = input("Date of Birth ")
#     try:
#         year, month, day = check_date(date_of_birth)
#     except:
#         sys.exit("Invalid date")
#     p = inflect.engine()
#     date_of_birth =  date(int(year), int(month), int(day))
#     today = date.today()
#     diff = today - date_of_birth
#     minutes = diff.days * 24 * 60
#     words = p.number_to_words(minutes, andword = "")
#     print(f"{words} minutes")
    
    
# def check_date(date_of_birth):
#     if re.search(r"^[0-9]{4}\-[0-9]{2}\-[0-9]{2}$", date_of_birth):
#         year, month, day = date_of_birth.split("-")
#         return year, month, day


# if __name__ in "__main__":
#     main()

"""




from datetime import date
from datetime import timedelta
import re
import sys
import operator
import inflect


def main():
    try:
        date_birth = convert(input("Date of Birth: ")).capitalize()
        print(date_birth)
    except:
        sys.exit("Invalid date")
  
def convert(s):
        matches = re.search(r"^([1-2][0-9][0-9][0-9])-([0-2][0-9])-([0-2][0-9])$", s)
        if matches:
            years = int(matches.group(1)) 
            months = int(matches.group(2)) 
            days = int(matches.group(3))
            date_birth_new = date(years,months,days)
            life = operator.__sub__(date.today(),date_birth_new)
            life_minutes = life.days * 24 * 60
            p = inflect.engine()
            words = p.number_to_words(life_minutes)
            new_words = words.replace( " and", "")
            return f"{new_words} minutes"
        
if __name__ == "__main__":
    main()




