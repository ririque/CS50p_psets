import random


def main():
    level = get_level()
    score = solution(level)
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n < 0:
                continue
            elif n in [1, 2, 3]:
                return n
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x,y


def calculation(x, y):
    tries = 1
    while tries <= 3:
        try:
            ans = int(input(f"{x} + {y} = "))
            if ans == (x + y):
                return True
            elif ans != (x + y):
                tries += 1
                print("EEE")
                continue
        except ValueError:
            tries += 1
            print("EEE")
            return False
    print(f"{x} + {y} = {(x+y)}")


def solution(level):
    rounds = 1
    score = 0
    while rounds <= 10:
        x,y = generate_integer(level)
        response = calculation(x,y)
        if response == True:
            score += 1
        rounds += 1
    return score


if __name__ == "__main__":
    main()
