from datetime import date
import inflect
import sys


def main():
    """Main function"""
    dob = input("Date of Birth: ")
    if is_valid(dob): print(days_to_words(calculate(dob)))

def is_valid(bday):
    if "-" in bday:
        if len(bday.split("-")[0]) != 4 or len(bday.split("-")[1]) != 2 or len(bday.split("-")[2]) != 2: raise ValueError("Invalid Date")
        try:
            x = date(int(bday.split("-")[0]), int(bday.split("-")[1]), int(bday.split("-")[2]))
            return True
        except ValueError:
            sys.exit("Invalid Date")
    else: sys.exit("Invalid Date")

def calculate(bday):
    """Calculate days since bday"""
    dob = date(int(bday.split("-")[0]), int(bday.split("-")[1]), int(bday.split("-")[2]))
    days = date.today() - dob
    return days.days

def days_to_words(num):
    """Returns a string containg amound of minutes"""
    p = inflect.engine()
    return p.number_to_words((int(num)*1440), andword="").capitalize() + " minutes"

if __name__ == "__main__":
    main()