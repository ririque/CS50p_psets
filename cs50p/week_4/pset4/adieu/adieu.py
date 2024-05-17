import inflect
p = inflect.engine()


def main():
    x = adieu("Name: ")
    print(f"\nAdieu, adieu, to {x}")


def adieu(prompt):
    name_list = []
    while True:
        try:
            n = input(prompt).title().strip()
            name_list.append(n)
        except EOFError:
                group = p.join(name_list)
                return group


if __name__ == "__main__":
    main()
