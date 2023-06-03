import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    if match := re.search(r'src="(.+)"', s):
        if link := re.sub(r"http(s)?://(www)?(\.)?youtube\.com/embed/", "https://youtu.be/", match.group(1) ):
            if "youtu.be" in link: return link
    # if match := re.search(r'src="http(?:s)?://www\.youtube\.com/embed/(\w+)"(?:.+)', s):
    #     return f"https://youtu.be/{match.group(1)}"
    else: return None


if __name__ == "__main__":
    main()