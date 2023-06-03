def main():
    while True:
        try:
            fuel_level(input("Fraction: "))
            break
        except (ValueError, ZeroDivisionError, NameError):
            pass

def fuel_level(x):
    # return either E or F (Empty/Full) or a percentage
    x = str.split(x, "/")
    fuel = int(x[0]) / int(x[1]) * 100
    if int(x[0]) > int(x[1]):
        pass
    elif fuel >= 99:
        print("F")
    elif fuel <= 1:
        print("E")
    else:
        print(f"{int(round(fuel))}%")
main()
