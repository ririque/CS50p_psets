def main():
   outdated("Date: ")


def outdated(date):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    m = d = y = ""
    while True:
        n = input(date)
        if "/" in n:
            m, d, y = n.split("/")
        else:
            m, d, y = n.replace(",", "").split()
            if m in months:
                m = months.index(m) + 1
            else:
                continue
        try:
            d = int(d)
            y = int(y)
            m = int(m)
            if d > 31 or m > 12:
                continue
        except ValueError:
            continue
        break

    print(f"{y}-{m:02}-{d:02}")


main()
