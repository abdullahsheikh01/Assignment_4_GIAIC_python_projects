# Problem: Write a function that takes a list of numbers and returns the sum of those numbers.
import sys
def sum_many_nums(nums:list[float])->float:
  sum:float = 0.0
  for _ in nums:
    sum+=_
  return sum
def main():
  try:
    nums_list : list[float] = [2,3,6.7,32.4,-9.3]
    sum : float = sum_many_nums(nums_list)
    nums : str = ", ".join(map(str,nums_list))
    sys.stdout.write(f"Sum of {nums} is {sum}")
  except:
    print("An Unknown Error Occured!")
if __name__ == '__main__':
    main()