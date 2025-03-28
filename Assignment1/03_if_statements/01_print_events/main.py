"""
Problem: Write a program that prints the first 20 even numbers. 
There are several correct approaches, but they all use a loop of some sort. 
Do no write twenty print statements
"""
def main():
  print("The First 20 even numbers are: ")
  for _ in range(0,20):
      print(_*2)
if __name__ == '__main__':
    main()