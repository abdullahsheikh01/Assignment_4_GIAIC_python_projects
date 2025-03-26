""" Problem: Fill out the function get_last_element(lst) which takes in a list lst 
as a parameter and prints the last element in the list. The list is guaranteed to 
be non-empty, but there are no guarantees on its length."""
def get_lst():
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst
def main():
  lst : list = get_lst()
  if len(lst) == 0:
    print("You do not enter any element in the list")
  else:
    print("The Last Element of the list is:",lst[len(lst)-1])
if __name__ == '__main__':
    main()