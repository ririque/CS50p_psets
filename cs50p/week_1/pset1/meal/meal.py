def main():
    t = input("What time is it? ")
    h = convert(t)
    if 7.0 <= h <= 8.0:
        print("breakfast time")
    elif 12.0 <= h <= 13.0:
        print("lunch time")
    elif 18.0 <= h <= 19.0:
        print("dinner time")


def convert(time):
    time = time.split(":")
    minutes = float(time[1]) / 60
    return(float(time[0]) + minutes)


if __name__ == "__main__":
    main()
