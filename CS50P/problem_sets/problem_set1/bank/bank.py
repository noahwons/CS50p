# --- Goal: Prompt user for a greeting. If greeting begins with "hello" output $0. If greeting starts with an "h"(but not hello), output $20. Otherwise, output $100.

# --- The greeting variable automatically converts the user's input into a lowercase phrase, void of whitespace before or after

# --- Main then determines if the greeting contained the specified phrases

def main():
    greeting = str.strip(str.casefold(str(input("Greeting: "))))
    if str.startswith(greeting, "hello"):
        print("$0")
    elif str.startswith(greeting, "h"):
        print("$20")
    else:
        print("$100")

main()