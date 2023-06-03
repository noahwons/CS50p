# pretty formal
from tabulate import tabulate
import csv
import sys

menu = []
place = []

def main():
    """The main function"""
    if check_cmnd_length():
        append_table()
        print(tabulate(menu, headers="keys", tablefmt="grid"))

def append_table():
    """get the first argument and the information within the file"""
    try:
        with open(f"{sys.argv[1]}") as file:
            dictreader = csv.DictReader(file)
            reader = csv.reader(file)
            for row in dictreader:
                if "Sicilian Pizza" in row:
                    menu.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
                elif "Regular Pizza" in row:
                    menu.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
    except FileNotFoundError:
        sys.exit("File does not exist")

def check_cmnd_length():
    """Checks the length of command line arg or the file type"""
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            return True
        else:
            sys.exit("Not a CSV ffile")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

main()