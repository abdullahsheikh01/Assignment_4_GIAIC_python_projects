# A program which converts Temprature of Farenheit into Celsisus
import sys
def main():
    try:
        BOLD_ITALIC = "\033[1;3m"
        RESET = "\033[0m"
        sys.stdout.write(RESET)
        sys.stdout.write("Enter Temprature in Fareheit "+BOLD_ITALIC)
        degrees_fahrenheit : float = float(input())
        sys.stdout.write(RESET)
        degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
        print(f"Temprature: {BOLD_ITALIC}{degrees_fahrenheit}{chr(176)}F = {RESET}{degrees_celsius}{chr(176)}")
    except:
        sys.stdout.write(RESET)
        BOLD = "\033[1m"
        print(f"{BOLD}Write Fahrenheit in Numbers!")
        main()
if __name__ == '__main__':
    main()