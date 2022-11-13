# gfg practice list(Basic)
# Program for How to check if a given number is Fibonacci number
print('Enter number to check if given number is Fibonacci number or not!')
n = int(input('Enter the number:- '))
a, b, c = 0, 1, 1
if n == 0 or n == 1:
    print('Yes')
else:
    while a<n:
        a = b + c
        c = b
        b = a
    if a == n:
        print('Yes')
    else:
        print('No')
"""
Enter number to check if given number is Fibonacci number or not!
Enter the number:- 5
Yes
"""
"""
Enter number to check if given number is Fibonacci number or not!
Enter the number:- 7
No
"""
