# --- The lower function takes a string "s" and changes the case to lower
def lower(s):
    return str.casefold(s)

# --- a variable "yell" asks for an input and calls to the lower function
yell = lower(input())

print(yell)

