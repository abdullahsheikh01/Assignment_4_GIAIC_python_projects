# A program Which gives square of user given number
import sys
def main():
    BOLD_ITALIC = "\033[1;3m"
    RESET = "\033[0m"
    try:
      sys.stdout.write("Give Number to get its square: "+BOLD_ITALIC)
      num : float = float(input())
      sys.stdout.write(RESET)
      print(f"The Square of {BOLD_ITALIC}{num}{RESET} is {num*num}")
    except:
      BOLD = "\033[1m"
      sys.stdout.write(BOLD)
      print("Give Valid Number")
      sys.stdout.write(RESET)
      main()

if __name__ == '__main__':
    main()