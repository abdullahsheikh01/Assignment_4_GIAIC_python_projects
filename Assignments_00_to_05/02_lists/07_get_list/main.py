"""Problem: Write a program which continuously asks the user to enter values
which are added one by one into a list. When the user presses enter without
typing anything, print the list."""
import sys
def main():
  BLUE = "\033[94m"
  RESET = "\033[0m" 
  try:
      lst : list = []
      sys.stdout.write("Enter Element of list or to skip press enter "+BLUE)
      elem = input()
      while elem!="":
        lst.append(elem)
        sys.stdout.write(RESET+"Enter Element of list or to skip press enter "+BLUE)
        elem = input()
      sys.stdout.write(RESET)
      if len(lst) == 0:
        print("Your List is Empty Because you not add any value")
      else:
        print("Your List",lst)
  except:
    print("Unknown Error Occured!")
if __name__ == '__main__':
    main()