# --- Goal: Prompt user for vanity plate, output "Valid" if requirements are met, or "Invalid" if they are not.

# Restrictions: Must start with two letters, maximum of 6 chars and minimum of 2, numbers must come at the end. First number used cannot be 0. No periods, spaces, or punctuatiuon marks

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# determine if plate is valid
def is_valid(s):
    # punctuation variable contains unwatned punctuation
    if (len(s) >= 2) and (len(s) <= 6):
        if starts_withlttr(s):
            if req_3(s):
                return True
            else:
                return False

def starts_withlttr(s):
    if str.isalpha(s[0:2]):  # if the first two chars in string s are not alphabetic
        return True
    else:
        return False

def req_3(s):
    punctuation = ["?", "!", " ", ".", ","]
    for i in range(len(s)):
        if s[i].isnumeric():
            if s[i] == "0":
                return False
            break
    for i in range(len(s)):
        if s[i].isnumeric():
            if not s[i:len(s)].isnumeric():
                return False
            for punc in range(len(punctuation)):
                if s[i] == punctuation[punc]:
                    return False
    return True

main()