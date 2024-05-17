from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    print(f"{valid_date()} minutes")


def valid_date():
    try:
        y, m, d = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")
    return check_date(y, m, d)


def check_date(year, month, day):
    try:
        bday = date(int(year), int(month), int(day))
    except ValueError:
        sys.exit("Invalid Date")
    today = date.today()
    diff = today - bday
    min = int(diff.total_seconds() / 60)
    w_min = p.number_to_words(min, andword="")
    return w_min.capitalize()


if __name__ == "__main__":
    main()
