def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    elif not s.isalnum():
        return False
    elif not (s[0:2].isalpha()):
        return False
    num1= len(s)-1
    for i in s:
        if i.isnumeric():
            if i == '0':
                return False
            num1 = s.index(i)
            break
    for i in s:
        if s.index(i) <= num1:
            pass
        else:
            if i.isalpha():
                return False

    return True


if __name__ == "__main__":
    main()
