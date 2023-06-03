import sys
import csv

students = []

def main():
    check_cmndline()
    reformat_names()
    write_new_file()

def check_cmndline():
    """Verifies command line args"""
    if len(sys.argv) > 3: sys.exit("Too many command-line arguments")
    if len(sys.argv) < 3: sys.exit("Too few command-line arguments")
    try:
        with open(sys.argv[1]) as file:
            pass
    except FileNotFoundError: sys.exit(f"Could not read {sys.argv[1]}")

def reformat_names():
    """Reformats the file by splitting name into first and last"""
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            students.append({"name": row[0], "home": row[1]})

def write_new_file():
    """Creates a new CSV file that contains the reformatted First, Last, House"""
    with open(sys.argv[2], "w") as file:
        writer = csv.writer(file)
        for student in students:
            full_name = student["name"].split(',')
            if student["name"] != "name":
                writer.writerow([full_name[1].lstrip(), full_name[0], student["home"]])
            else:
                writer.writerow(["first","last","house"])

main()