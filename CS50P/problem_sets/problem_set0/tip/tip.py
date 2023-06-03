# --- Main function contains two variables, each of which calling to two seperate functions, then multiplies these variables to calculate a total tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# --- The dollars to float functiont takes a string as an input and turns that string into a float
def dollars_to_float(d):
    d = str.replace(d,"$","")
    x = float(str(d))
    return x

# --- Turns percent into float
def percent_to_float(p):
    p = str.replace(p,"%","")
    y = float(p) / 100
    return y


main()