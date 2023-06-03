def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (len(s) >= 2) and (len(s) <= 6):
        if str.isalpha(s[0:2]):
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
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()
