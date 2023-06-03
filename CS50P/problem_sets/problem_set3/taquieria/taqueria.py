menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0.00

def main():
    while True:
        try:
            ask_user()
        except EOFError:
            print("\n")
            return False
        except KeyError:
            pass

def ask_user():
    # Print the price of the item
    menu_total(str.title(input("Item: ")))
    print(f"Total: $""%.2f" % total)

def menu_total(item):
    # Determine cost of item
    cost = float(menu[item])
    if item in menu:
        global total
        total = (total + cost)
        return total
    else:
        return False
main()