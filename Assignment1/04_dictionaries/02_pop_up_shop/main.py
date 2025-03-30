""" Problem: Write a program that loops through a dictionary of fruits, prompting the user to
see how many of each fruit they want to buy, and then prints out the total combined 
cost of all of the fruits."""
import sys
fruits_with_price : dict[str,int] = {
    "Mango(kg)":110,
    "Pear(kg)":100,
    "Melon(kg)":90,
    "Watermelon(kg)":150,
    "Apple(kg)":70,
    "Banana(Dozens)":40
}
fruits_with_quantity : dict[str,float] = {}
BOLD = "\033[1m"
RESET = "\033[0m" 
BOLD_ITALIC = "\033[1;3m"
def main():
    try:
        for _ in fruits_with_price:
            sys.stdout.write(f"How many {_} you want?(Price: PKR {fruits_with_price[_]}) "+BOLD_ITALIC)
            quantity:float = input()
            if quantity=="":
                quantity = 0
            elif float(quantity)<=-1:
                print("Quantity can't be negative")
                exit(0)
            quantity = float(quantity)
            fruits_with_quantity[_] = quantity
            sys.stdout.write(RESET)
        print("You buy: ")
        total : int = 0
        for _ in fruits_with_quantity:
            print(f"You buy {fruits_with_quantity[_]} {_} which costs PKR {fruits_with_price[_]*fruits_with_quantity[_]}")
            total+=fruits_with_price[_]*fruits_with_quantity[_]
        print(f"Your total Bill is {total}")
    except:
        print("Please Write Quantity in Positive Numbers")
if __name__ == '__main__':
    main()