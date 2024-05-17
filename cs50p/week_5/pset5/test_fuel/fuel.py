def main():
    x = gauge(convert(input("Fraction")))
    print(x)


def convert(fraction):
    while True:
        try:
            n = fraction.split('/')
            x = int(n[0])
            y = int(n[1])
            z = x/y
            if z <= 1:
                p = int(z * 100)
                return p
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <=1:
        return "E"
    elif percentage >=99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()
