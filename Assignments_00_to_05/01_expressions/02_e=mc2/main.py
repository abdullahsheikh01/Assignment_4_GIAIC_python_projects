# Write a program that continually reads in mass from the user and then outputs
# the equivalent energy using Einstein's mass-energy equivalence formula 
# (E stands for energy, m stands for mass, and C is the speed of light):
import sys
def main():
  BOLD = "\033[1m"
  RESET = "\033[0m" 
  BOLD_ITALIC = "\033[1;3m"
  try:
    sys.stdout.write("Enter The Mass in kilogram(kg) "+BOLD_ITALIC)
    m : float = float(input())
    sys.stdout.write(RESET)
    c :int = 299792458
    e : float = m*(c**2)
    print("e = m * C^2")
    print(f"m = {BOLD_ITALIC}{m}{RESET}kg")
    print(f"c = {c}m/s")
    print(f"The final Answer\n e = {e}Joules")
  except:
    sys.stdout.write(BOLD)
    print(f"Give Valid Number!")
    sys.stdout.write(RESET)
    main()
if __name__ == '__main__':
    main()