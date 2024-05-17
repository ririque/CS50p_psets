import sys
import os

def main():
    len_of_arg()
    print(read_file())


def len_of_arg():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments.")


def read_file():
    split_tup = os.path.splitext(sys.argv[1])
    file_extension = split_tup[1]
    if file_extension == ".py":
        number_of_lines = 0
        with open(file = sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if len(line) > 0:
                    if line[0] != "#":
                        number_of_lines += 1
            return number_of_lines
    else:
        raise FileNotFoundError("Not a Python file")


if __name__=="__main__":
    main()
