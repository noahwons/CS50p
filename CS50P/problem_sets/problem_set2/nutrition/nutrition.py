# --- Goal: take an input of a fruit and print the calories associated

# nutrition is a dictionary that contains each fruit and their respective calories

nutrition = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapes": "90",
    "honeydew Melon": "130",
    "kiwifruit": "90",
    "lemon" : "15",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80"
}

def main():
    # item is a case insensitive representation of the users input
    item = str.lower(input("Item: "))
    # if fruit is in the nutrition dictionary
    if item in nutrition:
        # print the calories associated with the fruit
        # nutrition[item] is the amount of calories associated with a fruit
        print("Calories: ", nutrition[item])

main()
