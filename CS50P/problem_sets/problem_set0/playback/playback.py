# --- A function elipse is created to replace whitespace with three periods
def elipse(s):
    return str.replace(s, " ", "...")
# --- A variable "prompt" calls the elipse function to take effect on a users input
prompt = elipse(input())
print(prompt)