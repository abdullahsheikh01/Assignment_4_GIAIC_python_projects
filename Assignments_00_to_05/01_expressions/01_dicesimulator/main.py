# Problem:
# Simulate rolling two dice, three times. Prints the results of each die roll.
import random
def main():
    try:
      for _ in range(1,4):
        print(f"Roll {_}: ")
        print(f"Dice1 = {random.randrange(1,7)} and Dice2 = {random.randrange(1,7)}")
    except:
      print("Unknown Error Occured")
if __name__ == '__main__':
    main()