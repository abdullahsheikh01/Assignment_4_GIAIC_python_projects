# This is a program to sum two numbers
def main():
    try:
        num1 : float = float(input("Enter First Number: "))
        num2 : float = float(input("Enter Second Number: "))
        sum : float = num1+num2
        print(f"The sum of {num1} and {num2} is {sum}")
    # Except Block for Value Error
    except:
        print("Give Values in Numbers")
        main()
# This ensures that the following code runs only when the script is executed directly
if __name__ == '__main__':
    main()