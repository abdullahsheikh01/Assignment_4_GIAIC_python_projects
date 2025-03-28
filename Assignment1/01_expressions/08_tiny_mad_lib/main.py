# Problem: Write a program which prompts the user for an adjective, then a noun,
# then a verb, and then prints a fun sentence with those words!
import sys
def main():
  RESET = "\033[0m" 
  BOLD_ITALIC = "\033[1;3m"
  try:
      SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my "
      sys.stdout.write("Enter an adjective "+BOLD_ITALIC)
      adjective : str = input()
      sys.stdout.write(RESET)
      sys.stdout.write("Enter a noun "+BOLD_ITALIC)
      noun : str = input()
      sys.stdout.write(RESET)
      sys.stdout.write("Enter a verb "+BOLD_ITALIC)
      verb : str = input()
      sys.stdout.write(RESET)
      print(f"{SENTENCE_START}{BOLD_ITALIC}{adjective} {noun} {verb}{RESET}!")
  except:
      print("Unknown Error Occured!")
if __name__ == '__main__':
    main()