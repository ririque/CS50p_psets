import random


def main():
    level = game("Level: ")
    gues = guess(level)
    print(gues)


def game(prompt):
    while True:
        try:
            n = int(input(prompt))
            level = random.randrange(n + 1)
            return level
        except ValueError:
            continue


def guess(level):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                continue
            elif guess < level:
                print("Too small!")
                continue
            elif guess > level:
                print("Too large!")
                continue
            elif guess == level:
                return "Just right!"
        except ValueError:
            continue


if __name__ == "__main__":
    main()
