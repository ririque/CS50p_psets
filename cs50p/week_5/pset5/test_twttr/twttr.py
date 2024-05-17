def main():
    word = input("Input: ")
    new = omit(word)
    print(f"Output: {new}")


def shorten(word):
    vows = ["a", "e", "o", "i", "u"]
    for vow in vows:
        if vow in word
            word = word.replace(vow, '')

    return word


if __name__ == "__main__":
    main()
