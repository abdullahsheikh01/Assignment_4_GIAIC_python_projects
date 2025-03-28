"""Problem:Fill out the function shorten(lst) which removes elements from the end of lst,
  which is a list, and prints each item it removes until lst is MAX_LENGTH items long.
  If lst is already shorter than MAX_LENGTH you should leave it unchanged."""
def shorten(lst:list,max_len:int)->None:
    if max_len>0:
        while len(lst) != max_len:
            lst.pop()
    else:
        print("Length of list can't be less than 1")
    return None
def main()->None:
    lst : list = [2,4,3,1,5,4,"Hello",True]
    print("Initial List: ",lst)
    shorten(lst,6)
    print("Updated List: ",lst)
    return None
if __name__ == '__main__':
    main()