""" 
Problem: Write a program which asks the user how tall they are and prints whether or not
they're taller than a pre-specified minimum height.
In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have 
minimum height requirements for safety reasons.
"""
import sys
def main():
    try:
        BOLD = "\033[1m"
        BOLD_ITALIC = "\033[1;3m"
        RESET = "\033[0m"
        minimum_height_in_inch : int = 50
        sys.stdout.write("Enter Your height in inches "+BOLD_ITALIC)
        user_height : float = float(input())
        sys.stdout.write(RESET)
        if user_height>0:
            if user_height>=minimum_height_in_inch:
                print("You are eligible to ride roller coasters")
            else:
                print("You are not eligible to ride roller coasters")
        else:
            sys.stdout.write(BOLD)
            print("Invalid Input height can't be less than 1")
            sys.stdout.write(RESET)
            main()
    except:
        sys.stdout.write(BOLD)
        print("Invalid Input Write height in positive numbers")
        sys.stdout.write(RESET)
        main()
if __name__ == '__main__':
    main()