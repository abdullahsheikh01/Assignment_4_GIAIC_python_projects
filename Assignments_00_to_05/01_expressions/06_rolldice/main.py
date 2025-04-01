# Problem: Simulate rolling two dice, and prints results of each roll as well as the total.
import random
def main():
    try:
      dice1 : int = random.randint(1,6)
      dice2 : int = random.randint(1,6)
      print(f"""Roll:
      Dice1: {dice1} Dice2: {dice2}
      Total: {dice1+dice2}""")
    except:
      print("Unknown Error Occurred!")
if __name__ == '__main__':
    main()