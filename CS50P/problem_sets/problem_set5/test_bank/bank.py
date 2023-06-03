def main():
    greeting = str(input("Greeting: "))
    print(f"${value(greeting)}")

def value(greeting):
    greeting = (greeting).strip().casefold()
    if str.startswith(greeting, "hello"):
        return 0
    elif str.startswith(greeting, "h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()