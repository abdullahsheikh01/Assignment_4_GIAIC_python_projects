"""
Problem: Write a simple joke bot. The bot starts by asking the user what they want. 
However, your program will only respond to one response: Joke.
If the user enters Joke then we will print out a single joke. Each time the joke is always
the same:
"""
import sys
def main()->None:
    BLUE = "\033[34m"
    RESET = "\033[0m"
    try:
        PROMPT : str = "What do you want? "
        JOKE : str = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
        SORRY : str = "Sorry I only tell jokes"
        sys.stdout.write(PROMPT+BLUE)
        user_input: str = input()
        sys.stdout.write(RESET)
        if user_input.upper() == "JOKE":
            print(JOKE)
        else:
            print(SORRY)
        return None
    except:
        print("Unknown Error Occured!")
        return None
    
if __name__ == '__main__':
    main()