""" Problem:
Write a program that prints out the calls for a spaceship that is about to launch. 
Countdown from 10 to 1 and then output Liftoff!
"""
def main()->None:
    try:
        for _ in range(0,10):
            print(10-_)
        print("Lift Off!")
        return None
    except:
        print("Unknown Error Occured!")
        return None
if __name__ == '__main__':
    main()