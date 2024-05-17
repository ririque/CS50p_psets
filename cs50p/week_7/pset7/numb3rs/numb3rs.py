import re
import sys 


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    matches = re.search(r"^(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])\.(\d|\d{2}|1\d{2}|2[0-4]\d|25[0-5])$", ip)
    if matches:
        group = ""
        group = f"{matches.group(1)}.{matches.group(2)}.{matches.group(3)}.{matches.group(4)}"
        return True
    else:
        return False


if __name__ == "__main__":
    main()
