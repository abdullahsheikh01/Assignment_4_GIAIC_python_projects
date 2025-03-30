# Problem: Guess My Number Program
import random
def main():
    try:
      random_num : int = random.randint(0,99)
      user_guess_num : int = -1
      while not user_guess_num == random_num:
        user_guess_num : int = int(input("Enter Your Guess: "))
        if user_guess_num>99 or user_guess_num<0:
          print("Your guess is out of the range of guess number which is 0 to 99")
        elif user_guess_num==random_num:
          print("Yahoo! You guessed the number")
        elif user_guess_num>random_num:
          remainder : int = user_guess_num-random_num
          if remainder>=10:
            print("Your guess is  too high!")
          else:
            print("Your guess is little high!")
        elif user_guess_num<random_num:
          remainder : int = random_num-user_guess_num
          if remainder>=10:
            print("Your guess is too low!")
          else:
            print("Your guess is little low!")
    except:
      print("Enter Guess in Integers")
if __name__ == '__main__':
    main()