import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to (0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$", s):
        t1 = new_hour(matches.group(1), matches.group(2), matches.group(3))
        t2 = new_hour(matches.group(4), matches.group(5), matches.group(6))
        return f"{t1} to {t2}"
    else:
        raise ValueError


def new_hour(hr, m, pd):
    if hr == "12":
        if pd == "AM":
            hrs = "00"
        else:
            hrs = "12"
    else:
        if pd == "AM":
            hrs = f"{int(hr):02}"
        else:
            hrs = f"{int(hr)+12}"
    if m == None:
        minute = "00"
    else:
        minute = f"{int(m):02}"
    return f"{hrs}:{minute}"


if __name__ == "__main__":
    main()
