import os
import csv
import sys


def main():
    check_file()


def check_file():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments.")
    else:
        split_tup = os.path.splitext(sys.argv[1])
        file_extension = split_tup[1]
        if file_extension != ".csv":
            sys.exit("Not a csv file!")
        else:
             letter_version(sys.argv[1],sys.argv[2])


def letter_version(input, output):
    try:
        with open(input) as input:
            reader = csv.DictReader(input)
            with open(output, 'w') as output:
                head = ['first','last', 'house']
                writer = csv.DictWriter(output, fieldnames = head)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last":last, "house":house})

    except FileNotFoundError:
                sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()
