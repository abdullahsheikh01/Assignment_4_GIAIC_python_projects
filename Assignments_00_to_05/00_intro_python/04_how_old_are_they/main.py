# It is a program which resolving this age-related  riddle:
"""Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen"""
def main():
    try:
        anton_age : int = 21
        beth_age : int = anton_age+6
        chen_age : int = beth_age+20
        drew_age : int = chen_age+anton_age
        ethan_age = chen_age
        freinds_names : list [str] = ["Anton","Beth","Chen","Drew","Ethan"]
        friends_ages : list[int] = [anton_age,beth_age,chen_age,
                                    drew_age,ethan_age]
        for _ in freinds_names:
            print(f"{_} is {friends_ages[freinds_names.index(_)]}")
    except:
        print("Anonymous Error Occured!")
if __name__ == '__main__':
    main()