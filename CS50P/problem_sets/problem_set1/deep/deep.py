# -- Program promts user for the answer to the "Great Question Of life" and answers "Yes" to any form of 42 (forty-two, forty two)

# --- Functions are implemented to convert the user's input to lowercase and remove un-necissary whitespace

# --- The main funciton determines if the user has inputted a correct answer

def main():
    question = str.lower(str.strip(str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? "))))
    if question == "42" or question == "forty two" or question == "forty-two":
        print("Yes")
    else:
        print("No")
main()