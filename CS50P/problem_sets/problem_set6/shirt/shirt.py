import sys
from PIL import Image, ImageOps

def main():
    check_cmndline()
    transform_image()

def check_cmndline():
    """Verifies that the command line arguments fit the given criteria"""
    if len(sys.argv) > 3: sys.exit("Too many command-line args")
    if len(sys.argv) < 3: sys.exit("Too few command-line args")
    if (sys.argv[1].lower().endswith(".jpg") == False) and (sys.argv[1].lower().endswith(".jpeg") == False) and (sys.argv[1].lower().endswith(".png") == False): sys.exit("Invalid Input")
    if (sys.argv[2].lower().endswith(".jpg") == False) and (sys.argv[2].lower().endswith(".jpeg") == False) and (sys.argv[2].lower().endswith(".png") == False): sys.exit("Invalid Input")
    arg1, arg2 = sys.argv[1].split('.'), sys.argv[2].split('.')  # Assign arg1, arg2 to the extensions of each respective command-line argument
    if arg1[1] != arg2[1]: sys.exit("Input and output have different extensions")
    try:
        with open(sys.argv[1]) as file1:
            pass
    except FileNotFoundError:
        sys.exit("One or more of the files does not exist")

def transform_image():
    """Transforms the image based on the given requirements"""
    shirt = Image.open("shirt.png")
    size = shirt.size
    image = Image.open(sys.argv[1])
    shirt_resized = ImageOps.fit(shirt, (size))
    image_resized = ImageOps.fit(image, (size))
    image_resized.paste(shirt_resized, shirt_resized)
    image_resized.save(sys.argv[2])

main()