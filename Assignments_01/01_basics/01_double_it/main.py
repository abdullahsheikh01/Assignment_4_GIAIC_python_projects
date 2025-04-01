"""
Problem: Write a program that asks a user to enter a number. Your program will 
then double that number and print out the result. It will repeat that process 
until the value is 100 or greater.
"""
def main()->None:
    try:
      curr_value : float = float(input("Enter Number: "))
      if not curr_value<=0:
        while not curr_value>=100:
          curr_value = curr_value*2
          print(curr_value)
      else:
        print("Please Enter Number which is greater than 0")
      return None
    except:
      print("Please Give Number as input")
      main()
      return None
if __name__ == '__main__':
    main()