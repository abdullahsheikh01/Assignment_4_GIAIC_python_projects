import time
def main():
    try:
        t : int = int(input("Enter Time in Seconds: "))
        while t:
            minutes,seconds = divmod(t,60)
            timer : str = f"0{minutes}:0{seconds}"
            print(timer,end="\r")
            time.sleep(1)
            t-=1
        print("Timer Completed!")
        return None
    except:
        print("Please Enter Time in seconds in integers")
        return None
if __name__ == "__main__":
    main()
