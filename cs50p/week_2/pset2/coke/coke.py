def main():
    coke_machine()


def coke_machine():
    a = 50
    while True:
        print(f"Amount Due: {a}")
        n = int(input("Insert Coin: "))
        if n in (25, 10, 5) and n<a:
            a -= n
        elif n == a or n > a:
            n -= a
            print(f"Change Owed: {n}")
            break


main()


