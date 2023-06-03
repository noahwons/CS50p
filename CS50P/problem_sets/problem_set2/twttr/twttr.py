# --- Goal: Remove vowels from inputted text

def main():
    twttr = no_vowels(input("Input: "))
    print(twttr)

# no vowels goal is to remove vowels
def no_vowels(input):
    # 2 lists for uppercase and lowercase vowels
    vowel = ["a", "e", "i", "o", "u"]
    upper_vowel = ["A", "E", "I", "O", "U"]
    # Itterates over each char in the input
    for char in input:
        # for each char in the range of the length of vowel
        for i in range(len(vowel)):
            # if char is uppercase or lwoercase vowel
            if char == vowel[i] or char == upper_vowel[i]:
                input = str.replace(input, char, "")
    return input

main()