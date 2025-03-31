""" Problem: Write a program that displays the terms in the Fibonacci sequence, starting 
with Fib(0) and continuing as long as the terms are less than 10,000 
(you should store this value as a constant!).
"""
def main()->None:
    try:
        max_term : int = 10000
        curr_term : int = 0
        next_term : int = 1
        while curr_term<=max_term:
            print(curr_term)
            term_after_next : int = curr_term+next_term
            curr_term = next_term
            next_term = term_after_next
        return None
    except:
        return None
if __name__ == '__main__':
    main()