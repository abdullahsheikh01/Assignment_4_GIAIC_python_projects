# An agreement bot which say its favouraite animal which is entered by user
def main():
    try:
        user_fav_animal : str = input("Enter Your Favouraite Animal ")
        BOLD_ITALIC = "\033[1;3m"
        print(f"My Favouraite Animal is also {BOLD_ITALIC}{user_fav_animal}")
    # Except Block For any error
    except:
        print("Anonymous Error Occured!")
if __name__ == '__main__':
    main()