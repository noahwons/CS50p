import random

def main():
    """Main Program"""
    level = get_level()
    questions = []
    score = 10
    wrong = 0
    q_num = 0
    while q_num < 10:
        ints = generate_integer(level)
        questions.append(ints)
        q_num += 1
    for i in range(len(questions)):
        while wrong != 3:
            answer = int(input(f"{questions[i][0]} + {questions[i][1]} = "))
            if answer == questions[i][0] + questions[i][1]:
                break
            if answer != questions[i][0] + questions[i][1]:
                print("EEE")
                wrong += 1
        if wrong == 3:
            print(f"{questions[i][0]} + {questions[i][1]} = {questions[i][0]+questions[i][1]}")
            score -= 1
            wrong = 0
    print(f"Score: {score}")


def get_level():
    """Get level user wants to play"""
    while True:
            try:
                level = int(input("Level: "))
                if level >= 1 and level <= 3:
                    break
                else:
                    pass
            except ValueError:
                pass
    return level


def generate_integer(level):
    """Generate integer (x) and (y) based on the level"""
    if level > 3 or level < 1:
        raise ValueError
    elif level == 1:
        x = random.randrange(10)
        y = random.randrange(10)
        return x, y
    elif level == 2:
        x = random.randrange(10, 100)
        y = random.randrange(10, 100)
        return x, y
    elif level == 3:
        x = random.randrange(100, 1000)
        y = random.randrange(100, 1000)
        return x, y


if __name__ == "__main__":
    main()
