# --- Goal: prompt user for camel case, output corresponding name in snake case
def main():
    camel = convert(input("camelCase: "))
    print(camel)

# --- The purpose of the convert funciton is to change the camel case into snake case

def convert(camel):
    # snake is set equal to "" so it can be replaced with _
    snake = ""
    # for loop looks for capital letters within camelcase
    for char in camel:
        if str.isupper(char):
            # if an uppercase letter is found, snake is replaced with an underscore and the uppercase letter is added onto it and converted to lower case
            snake = snake + "_" + str.lower(char)
        else:
            # an else statement is created to ensure that if no uppercase letter is detected, snake is equal to the char
            snake += char
    return snake

main()