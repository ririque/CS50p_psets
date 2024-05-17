#guess = 10 # single = is an assignment
def get_guess():
    guess = input("Enter a guess: ")
    return guess

def main():
    guess = get_guess()
    print(guess)
    if guess == "fifty":
        print("Correct")
    else:
        print("Incorrect")

main()
