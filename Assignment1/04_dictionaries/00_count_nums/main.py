""" Problem: This program counts the number of times each number appears in a list.
Use a dictionary to keep track of the information."""
import sys
BOLD = "\033[1m"
BLUE = "\033[94m"
RESET = "\033[0m"
def get_user_nums()->list[float]:
    try:
        nums : list[float] = []
        while True:
            sys.stdout.write("Enter Number Or to Stop Press Enter "+BLUE)
            num : float = input()
            sys.stdout.write(RESET)
            if num=="":
                break
            else:
                num = float(num)
                nums.append(num)
        print(nums)
        return nums
    except:
        sys.stdout.write(BOLD)
        print("Write Values in Numbers")
        sys.stdout.write(RESET)
def main():
    nums : list[float] = get_user_nums()
    nums_dict : dict[float:float] = {}
    if nums : 
      for _ in nums:
          if _  in nums_dict:
            nums_dict[_] +=1
          else:
            nums_dict[_] = 1
      print(nums_dict)
      for _ in nums_dict:
            print(f"{_} occcurs {nums_dict[_]} times")
if __name__ == '__main__':
    main()