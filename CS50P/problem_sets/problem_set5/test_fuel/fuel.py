def main():
    while True:
        try:
            x = gauge(convert(input("Fraction: ")))
            print(x)
            break
        except (ValueError, ZeroDivisionError, NameError):
            pass

def convert(fraction):
    fraction = fraction.split("/")
    if int(fraction[1]) == 0:
        print(int(fraction[1]))
        raise ZeroDivisionError
    elif int(fraction[0]) <= int(fraction[1]):
        percentage = int(fraction[0]) / int(fraction[1]) * 100
        return percentage
    else:
        raise ValueError

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{int(round(percentage))}%"

if __name__ == "__main__":
    main()
