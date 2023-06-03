# Using dict, code a grocery list program in uppercase when ctrl d is inputted, also nubered(total occurrences) in alphabetical order
grocery_items = {}

def main():
    while True:
        try:
            grocery_list()
        except EOFError:
            print_list()
            return False

def grocery_list():
    # determine number of occurrences and if a value exists, formatted to uppercase
    item = str.upper(input(""))
    if item in grocery_items:
        grocery_items[item] += 1
    else:
        grocery_items[item] = 1
    return grocery_items

def print_list():
    # print num of occurrences and item
    for key in sorted(grocery_items.keys()):
        print(grocery_items[key], key)

main()