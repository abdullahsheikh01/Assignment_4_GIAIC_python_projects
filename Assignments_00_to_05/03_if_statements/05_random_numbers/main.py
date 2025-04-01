# Problem: Print 10 random numbers in the range 1 to 100.
import random
def main():
    try:
      numbers : int = 10
      start_range : int = 1
      end_range : int = 100
      i : int = 0
      random_nums : list[int] = []
      while i<numbers:
        random_num : int = random.randint(start_range,end_range)
        random_nums.append(random_num)
        i+=1
      final_list = list(map(str,random_nums))
      print("Random Numbers: ", ",".join(final_list))
    except:
      print("Unknown Error Occured!")
if __name__ == '__main__':
    main()