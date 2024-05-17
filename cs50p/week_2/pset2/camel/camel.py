def main():
    name = snake_name()
    print(f"snake_name: {name}")


def snake_name():
    n = input("camelCase: ")
    snake_name=""
    for i in n:
        if i.isupper() and i != n[0]:
            snake_name += "_" + i.lower()
        else:
            snake_name +=i
    return snake_name


main()
