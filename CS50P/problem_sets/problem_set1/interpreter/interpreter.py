# --- Goal: promp user for arithemtic expression, calcuklate and output result as a flaoting-point value(one decimal place)

# --- In main exp contains the user's expression

# --- x, y, z, are all pieces of the expression seperated by the .split function

# --- The .split function allows for the three variables (x, y, z) to contain user input that is seperated buy a " " Ex: 1 + 1 -> x = 1, y = +, and z = 1

def main():
    exp = input("Expression: ")
    x, y, z = exp.split(" ")
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/":
        print(float(x) / float(z))
main()

