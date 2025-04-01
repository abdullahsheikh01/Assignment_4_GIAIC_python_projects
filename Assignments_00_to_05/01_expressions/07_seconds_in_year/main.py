# Problem: Use Python to calculate the number of seconds in a year, and tell the
# user what the result is in a nice print statemen
def main():
    try:
      days_in_year : int = 365
      days_in_leap_year : int = 366
      hours_in_day : int = 24
      minutes_in_hour : int = 60
      seconds_in_minute : int = 60
      seconds_in_year = seconds_in_minute*minutes_in_hour*hours_in_day*days_in_year
      seconds_in_leap_year = seconds_in_minute*minutes_in_hour*hours_in_day*days_in_leap_year
      print(f"There are {seconds_in_year} seconds in one year")
      print(f"There are {seconds_in_leap_year} seconds in one leap year")
    except:
      print("Unknown Error Occured!")
if __name__ == '__main__':
    main()