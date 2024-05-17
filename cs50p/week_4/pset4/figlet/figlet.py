from pyfiglet import Figlet as f
import sys
import random


def main():
    x = asci("Input: ")
    #Output the ascii font
    print("Output: \n" + x)


def asci(prompt):
    figlet = f()
    fig_list = figlet.getFonts()
    # Return the random ascii font
    if len(sys.argv) == 1:
        fig_list_random = random.choice(fig_list)
        figlet.setFont(font = fig_list_random)
        return figlet.renderText(input(prompt).strip())
    # Evaluate the selected font, find if the sys.argv is valid
    elif sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fig_list:
        # Check if the lenght if valid
        if len(sys.argv) == 3:
            figlet.setFont(font = sys.argv[2])
            return figlet.renderText(input(prompt).strip())
        # Exit if invalid
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
