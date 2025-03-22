# Problem: Converts feet to inches
import sys
def main():
  BOLD = "\033[1m"
  BOLD_ITALIC = "\033[1;3m"
  RESET = "\033[0m"
  try:
    sys.stdout.write("Enter Length in feet to convert in inches: ")
    sys.stdout.write(BOLD_ITALIC)
    feet : float = float(input())
    sys.stdout.write(RESET)
    print(f"{BOLD_ITALIC}{feet}{RESET} feet is {feet*12} inches")#There are 12 inches in one foot
  except:
    sys.stdout.write(BOLD)
    print("Give Feet in Inches")
    sys.stdout.write(RESET)
    main()
if __name__ == '__main__':
    main()