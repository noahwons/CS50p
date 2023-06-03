# --- Goal: determine weather to eat breakfast, lunch or dinner based on time of day. Challenge: implement (#:## am/pm, ##:## am/pm)

# Main calls to the convert function and uses basic logic to determine food to eat for a particualr time of dat (determined by convert function)

def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# --- convert function converts the time into a decimal form by using the .split function and basic arithmetic

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + float(minutes) / 60

# --- No clue what this last part does tbh but it doesnt work wo it

if __name__ == "__main__":
    main()