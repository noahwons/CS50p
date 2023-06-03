import re
import sys


def main():
    """main func"""
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    """Validates the IP address based on given criteria"""
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip.strip()):
        if int(matches.group(1)) <= 255 and int(matches.group(2)) <= 255 and int(matches.group(3)) <= 255 and int(matches.group(4)) <= 255:
            return True
        else: return False
    else: return False


if __name__ == "__main__":
    main()