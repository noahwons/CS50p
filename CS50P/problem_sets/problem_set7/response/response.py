import validators

def main():
    print(validate(input("What's your email? ")))

def validate(s):
    if validators.email(s): return "Valid"
    else: return "Invalid"

main()