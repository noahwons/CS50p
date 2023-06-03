
def main():
    twttr = shorten(input("Input: "))
    print(twttr)

def shorten(input):
    vowel = ["a", "e", "i", "o", "u"]
    upper_vowel = ["A", "E", "I", "O", "U"]
    for char in input:
        for i in range(len(vowel)):
            if char == vowel[i] or char == upper_vowel[i]:
                input = str.replace(input, char, "")
    return input

if __name__ == "__main__":
    main()