"""Write a program which asks a user for their age and lets them know if they can or
can't vote in the following three fictional countries.Around the world, different countries
have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and
Mayengua, the voting ages are very different:
the voting age in Peturksbouipo is 16 
(in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)
the voting age in Stanlau is 25 (in real life this is the voting age in the 
United Arab Emirates)
the voting age in Mayengua is 48 
(in real life, as far as we can tell, this isn't the voting age anywhere)
Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.
"""
import sys
def main():
    BOLD = "\033[1m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    try:
        sys.stdout.write("How old are you? "+BLUE)
        age : int = int(input())
        sys.stdout.write(RESET)
        if age>0:
            if age>=16:
                print("You can vote in Peturksbouipo where the age of voting is 16")
                if age>=25:
                    print("You also can vote in Stanlau where the age of voting is 25")
                else:
                    print("You cannot vote in Stanlau where the age of voting is 25")
                if age>=48:
                    print("You also can vote in Mayengua where the age of voting is 48")
                else:
                    print("You cannot vote in Mayengua where the age of voting is 48")
            else:
                print("You cannot vote in Peturksbouipo, Stanlau, and Mayengua\nbecause Peturksbouipo has voting age of 16 \n Stanlau has voting age of 25 \n Mayengua has voting age of 48")
        else:
            print("Age can not less than 1 Enter Valid Age: ")
            main()
    except:
        sys.stdout.write(RESET)
        sys.stdout.write(BOLD)
        print(f"Write valid input for age")
        sys.stdout.write(RESET)
        main()
if __name__ == '__main__':
    main()