import requests
import json
import sys


def main():
    print(bitcoin())


def bitcoin():
    try:
        if len(sys.argv) != 2:
            sys.exit("Missing command-line argument")
        elif isinstance(sys.argv[1], float):
            sys.exit("Command-line argument is not a number")

        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        o = response.json()
        usd_value = o["bpi"]["USD"]["rate_float"]
        coins = (float(sys.argv[1])*usd_value)
        
        return f"${coins:,.4f}"
    except requests.RequestException as er:
        print(er)


if __name__ == "__main__":
    main()
