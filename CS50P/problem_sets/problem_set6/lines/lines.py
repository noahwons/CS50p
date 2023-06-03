import sys

def main():
    """Main program"""
    if conditional_1():
        print(conditional_2())

def conditional_1():
    """Check length of the argument, determine end of string"""
    if len(sys.argv) > 2 or len(sys.argv) < 1:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python File")
    else:
        return True

def conditional_2():
    """Detect space or '#'"""
    lines_code = 0
    try:
        with open(f"{sys.argv[1]}") as file:
            for line in file:
                if not line.isspace():
                    if not line.lstrip().startswith("#"):
                        lines_code +=1
            return lines_code
    except FileNotFoundError:
        sys.exit("File does not exist")

main()