def main():
    list_grocery()


def list_grocery():
    grocery = {

    }
    while True:
        try:
            n = input().upper().strip()
            grocery[n] = grocery.get(n, 0) + 1
        except EOFError:
            print("\n")
            sor = sorted(grocery)
            for i in sor:
                print(f"{grocery[i]} {i}")
            break


main()
