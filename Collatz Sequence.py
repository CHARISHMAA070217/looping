'''
The rules for generating Collatz Sequence are:
If n is even:   n = n / 2
If n is odd:    n = 3n + 1
def printCollatz(n):
     
    # We simply follow steps
    # while we do not reach 1
    while n != 1:
        print(n, end = ' ')
 
        # If n is odd 
        if n & 1:
            n = 3 * n + 1
 
        # If even 
        else:
            n = n // 2
 
    # Print 1 at the end 
    print(n)
 
# Driver code 
printCollatz(6)
'''
