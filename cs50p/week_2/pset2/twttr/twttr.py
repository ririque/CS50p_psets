def main():
    new = omit()
    print(f"Output: {new}")


def omit():
    n = input("Input: ")
    new = ""
    for i in n:
        if i in ("a", "e", "o", "i", "u") or i in ("A", "E", "O", "I", "U"):
            new += ""
        else:
            new += i
            
    return new


main()
