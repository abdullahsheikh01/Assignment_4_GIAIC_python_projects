import sys
# An agreement bot which say its favouraite animal which is entered by user
def main():
    try:
        BOLD_ITALIC = "\033[1;3m"
        RESET = "\033[0m"
        sys.stdout.write("Enter Your Favouraite Animal "+BOLD_ITALIC)
        user_fav_animal = input()
        sys.stdout.write(RESET)
        print(f"My Favouraite Animal is also {BOLD_ITALIC}{user_fav_animal}!")
    # Except Block For any error
    except:
        print("Anonymous Error Occured!")
if __name__ == '__main__':
    main()