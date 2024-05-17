def main():
    x = fraction_tank("Fraction: ")
    print(x)


def fraction_tank(value):
    while True:
        try:
            n = input(value).split('/')
            x = int(n[0])
            y = int(n[1])
            z = x/y
            if 0.01 < z < 0.99:
                return (f'{round((x/y)*100)}%')
            elif z >= 0.99 and z <= 1.00:
                return "F"
            elif z <= 0.01:
                return "E"
        except (ValueError, ZeroDivisionError, ):
            pass


main()
