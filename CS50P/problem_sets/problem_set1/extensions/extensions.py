# --- Goal: Prompt user for file name, output the file's media type (case-insensitive)

# --- Main contains a variabl "file" that prompts the user for a file name, then removes case

def main():
    file = str.strip(str.casefold((input("File name: "))))

    # --- Within main multiple if/elif/else statements determine the MIME type of the file.

    if str.endswith(file,".gif"):
        print("image/gif")
    elif str.endswith(file,".jpg") or str.endswith(file,".jpeg"):
        print("image/jpeg")
    elif str.endswith(file,".png"):
        print("image/png")
    elif str.endswith(file,".pdf"):
        print("application/pdf")
    elif str.endswith(file,".txt"):
        print("text/plain")
    elif str.endswith(file,".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()