# Problem: Write a program that reads a year from the user and tells whether a given year is a leap year or not.
def main():
  try:
    year : int = int(input("Enter year to check its leap year or not "))
    if year>0:
      if year%4==0 and year%100==0:
        if year%400==0:
          print("That's a leap year")
        else:
          print("That's not a leap year")
      elif year%4==0:
        print("That's a leap year")
      else:
        print("That's not a leap year")
    else:
      print("Year can't be less than 1")
  except:
    print("Invalid Input!")
    main()
if __name__ == '__main__':
    main()