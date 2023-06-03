# Format dates
months = [
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


def main():
    while True:
        date = get_date()
        formatedDate = format(date)
        if formatedDate:
            print(format(date))
            break


def get_date():
    date = input("Date: ").strip()
    return date


def format(s):
    slashes = False
    for i in s:
        if i == "/":
            s = s.split("/")
            slashes = True
            break
        if i == " ":
             s = s.split(" ")
             break

    if s[0] in months and not slashes:
        if int(s[1].strip(",")) <= 31:
            month = months.index(s[0]) + 1
            if int(month) <= 12:
                if int(month) < 10:
                    month = f"0{month}"
                day = s[1]
                if "," in day:
                    day = s[1].strip(",")
                    if int(day) < 10:
                        day = f"0{day}"
                    year = s[2]
                    return f"{year}-{month}-{day}"

    elif len(s) == 3 and slashes:
        return format2(s)


def format2(s):
    try:
        month = s[0]
        day = s[1]
        year = s[2]
        if int(day) < 31 and int(month) <= 12:
            if int(day) < 10:
                day = f"0{day}"
            if int(month) < 10:
                month = f"0{month}"
            return f"{year}-{month}-{day}"
    except ValueError:
        pass


main()