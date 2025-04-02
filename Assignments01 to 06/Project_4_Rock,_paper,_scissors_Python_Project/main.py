import random
def main():
    try:
        user : str = input("What's your Choice?(R for Rock, S for Scissor and P for paper)").lower()
        computer : str = random.choice(["r","s","p"]).lower()
        print(f"You Choose {user}")
        print(f"User Choose {computer}")
        if user==computer:
            print("It's Tie")
        elif (user == "r" and computer == "s") or (user=="s" and computer=="p") or \
            (user=="p" and computer=="r"):
            print("You Win!")
        else:
            print("Computer Wins!")
        return None
    except:
        print("Unknown Error Occured!")
        return None
if __name__ == "__main__":
    main()