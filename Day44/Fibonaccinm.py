# gfg practice list(Basic)
# Program for n-th multiple of a number in Fibonacci Series
print('Enter to get n-th multiple of a number in Fibonacci Series')
x = int(input('Enter multiple number:- '))
y = int(input('Enter number:- '))


def find(k, n):
    a = 0
    b: int = 1
    i = 2
    while i != 0:
        c = a + b
        a = b
        b = c
        if b % k == 0:
            return n*i
        i += 1
    return


print("Position of n-th multiple of a number in Fibonacci Series:- ", find(y, x))
"""
Enter to get n-th multiple of a number in Fibonacci Series
Enter multiple number:- 5
Enter number:- 4
Position of n-th multiple of a number in Fibonacci Series:-  30
"""
