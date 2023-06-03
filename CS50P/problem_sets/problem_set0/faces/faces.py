# --- Main contains a variable prompt that asks the user for an input and calls the convert function on that input
def main():
    prompt = convert(input())
    print(prompt)

# --- The convert function replaces smiley faces found within the input with the actual emotocons and returns the specific s value.
def convert(s):
    s = str.replace(s,":)","🙂")
    s = str.replace(s,":(","🙁")
    return s
    
main()