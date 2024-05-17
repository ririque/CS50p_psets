def main():
    tacos("Item: ")


def tacos(prompt):
    items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0
    while True:
        try:
            n = input(prompt).title().strip()
            if n in items:
                total += items.get(n)
                print(f"Total: ${total:.2f}")
        except EOFError:
            print("\n", end="")
            break
        

main()
