def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    new_d = float(d.removeprefix("$"))
    return new_d


def percent_to_float(p):
    new_p = float(p.removesuffix("%"))/100
    return(round(new_p, 2))



main()
