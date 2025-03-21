# A Program which calculates the perimeter of Triangle🔺and allows only valid input as
# side of triangle
import sys
def main():
    try:
        BOLD_ITALIC = "\033[1;3m"
        RESET = "\033[0m"
        perimeter : float = 0
        for _ in range(1,3+1):
            sys.stdout.write(f"Write the length of side {_}? "+BOLD_ITALIC)
            side : float = float(input())
            if not (side<=0):
                perimeter+=side
                sys.stdout.write(RESET)
            elif side==0:
                print("Any Side of Triangle🔺 can't be Zero")
                sys.exit()
            else:
                print("Any Side of Triangle🔺 can't be negative")
                sys.exit()
        print(f"The Perimeter of Triangle🔺 is: {perimeter}")
    except:
        print("Side of Triangle🔺 should be positive number")

if __name__ == '__main__':
    main()