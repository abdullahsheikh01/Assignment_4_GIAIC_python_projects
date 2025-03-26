# fill out the add_three_copies(...) function which takes a list and some data and  then adds three copies of 
# the data to the list. Don't return anything and see what happens! Compare this process to the x = change(x) 
# example and note the differences.
import sys
def add_three_copies(list:list,data:str):
    for _ in range(1,4):
        list.append(data)
def main():
    BOLD = "\033[1m"
    RESET = "\033[0m" 
    BOLD_ITALIC = "\033[1;3m"
    try:
        sys.stdout.write("Enter a data to make copies: "+BOLD_ITALIC)
        data : str = input()
        sys.stdout.write(RESET)
        listt : list = []
        print("Before Change: ",listt)
        add_three_copies(listt,data)
        print("After Change: ",listt)
    except:
        print(BOLD+"Unknown Error Occured!")
if __name__ == '__main__':
    main()