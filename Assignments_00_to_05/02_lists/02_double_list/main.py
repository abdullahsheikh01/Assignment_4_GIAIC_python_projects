# Problem: Write a program that doubles each element in a list of numbers
def main():
    nums : list[int] = [3,6,4,2,34,4,-6,3,1]
    print(f"Starting List {nums}")
    for _ in range(0,len(nums)):
      nums[_] = nums[_]*2
    print(f"Ending List {nums}")
if __name__ == '__main__':
    main()