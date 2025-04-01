# Problem: Ask the user for two numbers, one at a time, and then print the
# result of dividing the first number by the second and also the remainder of the division.
import sys
def main():
  BOLD = "\033[1m"
  RESET = "\033[0m" 
  BOLD_ITALIC = "\033[1;3m"
  try:
    sys.stdout.write("Enter First Number: "+BOLD_ITALIC) 
    num1 : float = float(input())
    sys.stdout.write(RESET)
    sys.stdout.write("Enter Second Number: "+BOLD_ITALIC)
    num2 : float = float(input())
    sys.stdout.write(RESET)
    if num2==0:
      print("Cannot Divide by Zero")
    else:
      print(f"The division of {BOLD_ITALIC}{num1}{RESET} and {BOLD_ITALIC}{num2}{RESET} is {num1//num2} and the remainder is {num1%num2}")
  except:
    sys.stdout.write(BOLD)
    print("Give Input the Numbers")
    sys.stdout.write(RESET)
if __name__ == '__main__':
    main()