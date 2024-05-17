from emoji import emojize

def main():
    x = emojii("Input: ")
    print("Output: " + x)


def emojii(prompt):
    n = emojize(input(prompt))
    if ":thumbsup:" in n:
        return emojize(":thumbs_up:")
    elif ":earth_asia:" in n:
         return "hello, 🌏"
    else:
        return n


if __name__ == "__main__":
    main()
