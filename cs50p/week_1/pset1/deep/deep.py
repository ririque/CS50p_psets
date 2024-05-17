def main():
    deep(input("What is the Answer to Great Question of Life, the Universe and Everything? "))


def deep(n):
    match n:
        case "42" | "forty-two" | "forty two" | "FoRty TwO" | " 42 ":
            print("Yes")
        case "50" | "fifty":
            print("No")


main()
