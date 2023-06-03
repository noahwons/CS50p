import re
import sys


def main():
    """The main function"""
    print(convert(input("Hours: ")))


def convert(s):
    """Convets the input 's', an expected 12-hour format, to the 25-hour format according to the set criteria"""
    if match := re.search(r"^([0-9]+):?([0-9]+)? (AM|PM) to ([0-9]+):?([0-9]+)? (AM|PM)$", s.strip(), re.IGNORECASE):
        group1, group4 = 0, 0
        if match.group(5) and match.group(2):
            if int(match.group(1)) > 12 or int(match.group(2)) > 59 or int(match.group(4)) > 12 or int(match.group(5)) > 59: raise(ValueError)
            if int(match.group(1)) != 12 and match.group(3) == "PM": group1 = int(match.group(1)) + 12
            if int(match.group(4)) != 12 and match.group(6) == "PM": group4 = int(match.group(4)) + 12
            if int(match.group(4)) == 12 and match.group(6) ==  "PM": group4 = 12
            if int(match.group(1)) == 12 and match.group(3) == "AM":
                group1 = 0
                time1 = "00"
            if int(match.group(4)) == 12 and match.group(6) == "AM":
                group4 = 0
                time2 = match.group(4)
            if int(match.group(1)) < 10 and match.group(3) == "AM": time1 = f"0{match.group(1)}"
            if int(match.group(4)) < 10 and match.group(6) == "AM": time2 = f"0{match.group(4)}"
            if 12 > int(match.group(1)) >= 10 and match.group(3) == "AM": time1 = match.group(1)
            if 12 > int(match.group(4)) >= 10 and match.group(6) == "AM": time2 = match.group(4)
            if group1 > 0 and group4 > 0:
                return f"{group1}:{match.group(2)} to {group4}:{match.group(5)}"
            if group1 > 0 and group4 == 0:
                return f"{group1}:{match.group(2)} to {time2}:{match.group(5)}"
            if group4 > 0 and group1 == 0:
                return f"{time1}:{match.group(2)} to {group4}:{match.group(5)}"
            if group1 == 0 and group4 == 0:
                return f"{time1}:{match.group(2)} to {time2}:{match.group(5)}"
        else:
            if int(match.group(1)) > 12 or int(match.group(4)) > 12: raise(ValueError)
            if int(match.group(1)) != 12 and match.group(3) == "PM": group1 = int(match.group(1)) + 12
            if int(match.group(4)) != 12 and match.group(6) == "PM": group4 = int(match.group(4)) + 12
            if int(match.group(1)) == 12 and match.group(3) == "AM":
                group1 = 0
                time1 = "00"
            if int(match.group(4)) == 12 and match.group(6) == "PM":
                group4 = 12
                time2 = match.group(4)
            if int(match.group(1)) < 10 and match.group(3) == "AM": time1 = f"0{match.group(1)}"
            if int(match.group(4)) < 10 and match.group(6) == "AM": time2 = f"0{match.group(4)}"
            if 12 > int(match.group(1)) >= 10 and match.group(3) == "AM": time1 = match.group(1)
            if 12 > int(match.group(4)) >= 10 and match.group(6) == "AM": time2 = match.group(4)
            if group1 > 0 and group4 > 0:
                return f"{group1}:00 to {group4}:00"
            if group1 > 0 and group4 == 0:
                return f"{group1}:00 to {time2}:00"
            if group4 > 0 and group1 == 0:
                return f"{time1}:00 to {group4}:00"
            if group1 == 0 and group4 == 0:
                return f"{time1}:00 to {time2}:00"
    else: raise(ValueError)

if __name__ == "__main__":
    main()