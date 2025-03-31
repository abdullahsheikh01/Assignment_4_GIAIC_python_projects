import sys
def main()->None:
  BOLD = "\033[1m"
  BLUE = "\033[34m"
  RESET = "\033[0m"
  try:
    affirmation : str = "I am capable of doing anything I put my mind to."
    user_affirmation : str = ""
    while not affirmation == user_affirmation:
      sys.stdout.write("Write the following affirmation: \n"+affirmation+"\n"+BLUE)
      user_affirmation = input()
      sys.stdout.write(RESET)
      if user_affirmation == affirmation:
        print("That's Right!")
      else:
        print("That's Incorrect!")
    return None
  except:
    print("Unknown Error Occured!")
    return None
if __name__ == '__main__':
    main()