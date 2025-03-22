# Problem: Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle
# and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!
import sys
import math # For square root function
def main():
  BOLD = "\033[1m"
  RESET = "\033[0m" 
  BOLD_ITALIC = "\033[1;3m"
  try:
    sys.stdout.write(RESET+"Enter the length of AB "+BOLD_ITALIC)
    ab : float = float(input())
    sys.stdout.write(RESET+"Enter the length of AC "+BOLD_ITALIC)
    ac : float = float(input())
    c : float = (ab**2)+(ac**2)
    print(RESET+f"The Length of BC is {math.sqrt(c)}")
  except:
    print(BOLD+"Give Length of Sides in numbers")
    main()
if __name__ == '__main__':
    main()