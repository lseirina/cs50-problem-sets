"""
import sys
import csv
def main():
    check_comand_line_argv()
    students = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                split_reader = row["name"].split(",")
                students.append({"first":split_reader[1], "last":split_reader[0], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    
    with open("after.csv", "w") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["first","last","house"])
        writer.writeheader()
        for row in students:
            writer.writerow({"first":row["first"],"last":row["last"], "house":row["house"]})
def check_comand_line_argv():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit ("Too many command-line arguments")

if __name__=="__main__":
    main()

"""




import sys
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if sys.argv[1].endswith(".csv") == False and sys.argv[2].endswith(".csv") == False:
    sys.exit("Not a CSV file")

try:
    students = []
    with open(sys.argv[1], "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last_name, first_name = row["name"].split(",")
            student = {"first":first_name.lstrip(), "last":last_name, "house":row["house"]}
            students.append(student)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
    
with open(sys.argv[2], "w") as file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)
