def main():
    question = input("Greeting: ")
    answer = greeting(question)
    print(f"${answer}")
    
def greeting(n):
    if 'Hello' in n:
        return 0
    elif "H" in n:
        return 20
    else:
        return 100

main()
