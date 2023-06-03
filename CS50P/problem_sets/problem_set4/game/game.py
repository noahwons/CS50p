import random

while True:
    try:
        level = int(input("Level: "))
        num = random.randrange(1, level + 1)
        break
    except ValueError:
        pass

while True:
    try:
        guess = int(input("Guess: "))
        if guess == num:
            print("Just Right!")
            break
        if guess > num:
            print("Too Large!")
        if guess < num:
            print("Too small!")
    except ValueError:
        pass