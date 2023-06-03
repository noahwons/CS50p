import inflect
p = inflect.engine()

names = []

while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        names = p.join(names)
        print(f"\nAdieu, adieu, to {names}")
        break