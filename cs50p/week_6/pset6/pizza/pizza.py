from tabulate import tabulate
import csv
import sys
import os


def main():
    read_file()


def read_file():
   # checks if the lenght of the argv is correct
    if len(sys.argv) == 2:
        split_tup = os.path.splitext(sys.argv[1])
        file_extension = split_tup[1]
        if file_extension == ".csv":
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    print(tabulate(reader, headers = "keys", tablefmt="grid"))
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")


if __name__ == "__main__":
    main()
