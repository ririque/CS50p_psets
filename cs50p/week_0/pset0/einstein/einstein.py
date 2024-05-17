C = 300000000
def main():
    print(f"E: {calculation()}")

    
def calculation():
    m = int(input("m: "))
    return m *(pow(C, 2))


main()
