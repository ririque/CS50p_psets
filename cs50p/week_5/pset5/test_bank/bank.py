def main():
    question = input("Greeting: ")
    answer = value(question)
    print(f"${answer}")

def value(greeting):
    if 'Hello'in greeting[:5] or 'hello' in greeting[:5]:
        return 0
    elif "H" in greeting[0] or 'h' in greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
