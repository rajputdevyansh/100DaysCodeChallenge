# gfg practice list(Basic)
# Program for n-th Fibonacci number
print('Enter number to get n-th Fibonacci number')
a = int(input('Enter number:- '))


def fibonacci(n):
    if n < 0:
        print("Wrong Input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


print(f'n-th Fibonacci number:- {fibonacci(a)}')
"""
Enter number to get n-th Fibonacci number
Enter number:- -5
Wrong Input
n-th Fibonacci number:- None
"""
"""
Enter number to get n-th Fibonacci number
Enter number:- 15
n-th Fibonacci number:- 610
"""
