from PIL import Image, ImageOps
import os
import sys


def main():
    length()
    check_input_output()
    merge_images(sys.argv[1], sys.argv[2])

def length():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        pass


def check_input_output():
    split_input = os.path.splitext(sys.argv[1])
    input_extension = split_input[1]

    split_output = os.path.splitext(sys.argv[2])
    output_extension = split_output[1]
    supported_files = [".jpg", ".jpeg", ".png"]

    if input_extension.lower() not in supported_files:
        sys.exit("Invalid input")

    if output_extension.lower() not in supported_files:
        sys.exit("Invalid ouput")

    if input_extension.lower() != output_extension:
        sys.exit("Input and output have different extensions")

def merge_images(input_image, output_image):
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(input_image) as base_image:
                base_image = ImageOps.fit(base_image, shirt.size)
                base_image.paste(shirt, shirt)
                base_image.save(output_image)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
