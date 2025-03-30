phone_book : dict[str,str] = {}# Numbers in str because user can input number starting from 0
def lookup_contact():
  try:
    name : str = input("Enter Name of the contact: ")
    if name not in phone_book:
      print(f"There is no contact named {name} in your phonebook")
      main()
    else:
      print(f"{name}: {phone_book[name]}")
      main()
  except:
    print("Unknown Error Occured!")
def new_contact():
  try:
    print("Enter Following Fields to create new contact: ")
    name : str = input("Enter Name of the contact: ")
    number : int = input("Enter Number of the contact: ")
    int(number)
    phone_book[name] = str(number)
    return phone_book
  except:
    print("Enter Number in Numbers not enter any string in number")
    new_contact()

def menu_input():
  try:
    inputt : int = int(input("Press 1 for create new contact\nPress 2 to see all contacts\nPress 3 to lookup the contact and \nPress 4 to exit\n"))
    if inputt not in [1,2,3,4]:
      print("Please Write Number from the options ")
      menu_input()
    else:
      return inputt
  except:
    print("Please Write Number from the options")
def main():
    inputt: int = menu_input()
    if inputt:
      if inputt==1:
        new_contact()
        main()
      elif inputt==2:
        if len(phone_book) == 0:
          print("Your Phone book is empty")
          main()
        else:
          print("All Contacts: ")
          for _ in phone_book:
            print(f"{_}:{phone_book[_]}")
          main()
      elif inputt==3:
        lookup_contact()
      else:
        print("Good Bye!")
    else:
      main()
if __name__ == '__main__':
    print("Welcome to your Phonebook!")
    main()