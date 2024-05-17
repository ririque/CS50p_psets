def main():
    exp = input("Expression: ").split(" ")
    print(inter(exp))


def inter(n):
    x = n[0]
    y = n[1]
    z = n[2]
    if y == "+":
        return round(float(x) + float(z), 1)
    elif y == "-":
        return round(float(x) - float(z), 1)
    elif y == "*":
        return round(float(x) * float(z), 1)
    elif y == "/":
        return round(float(x) / float(z), 1)

main()
