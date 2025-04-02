import random
def main(x:int):
    try:
        random_number : int = random.randint(1,x)
        guessed_number : int = 0
        while random_number != guessed_number:
            guessed_number = int(input(f"Guess Number From 1 to {x}: "))
            if guessed_number >x or guessed_number<1:
                print(f"Your guess is out of range!(Range is: 1 to {x})")
            elif guessed_number >random_number:
                remainder : int = guessed_number-random_number
                if remainder>=10:
                    print("Your guess is too high!")
                else:
                    print("Your guess is little high!")
            elif guessed_number<random_number:
                remainder : int = random_number-guessed_number
                if remainder>=10:
                    print("Your guess is too low!")
                else:
                    print("Your guess is little low!")
        print("You guess correct Number!")
        return None
    except ValueError:
        print("Please write values in integers")
        return None
    except:
      print("An Unknown Error Occured!")
if __name__ == "__main__":
    main(220)