import validators


def main():
    print(check_email(input("What's your email addres? ")))


def check_email(s):
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
