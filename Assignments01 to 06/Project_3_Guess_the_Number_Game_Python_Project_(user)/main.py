import random
def main(x:int):
  try:
    start : int = 1
    end : int = x
    feedback : str = ""
    while feedback!="c":
      guess : int = random.randint(start,end)
      print(guess)
      feedback = input("This number is correct(c) or little low(l) or little high(h) or very low(vl) or very high(vh): ")
      if feedback.lower() == "l":
        start = guess+1
      elif feedback.lower() == "h":
        end = guess-1
      elif feedback.lower() == "vl":
        start = guess+10
      elif feedback.lower() == "vh":
        end = guess-10
    print("Yah! computer guessed correct number!")
    return None
  except:
    print("Unknown Error Occured")
    return None
if __name__ == "__main__":
  print("Welcome to Number Guessing Game.\n In this game you will choose a \
  \nnumber and computer will guess the number(Range: 1 to 220).\
\nYou have to give feedback about his guess!")
  main(220)