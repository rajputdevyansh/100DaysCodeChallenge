# gfg practice list(Basic)
# Program to check whether a number is Prime or not
print('Enter number to check prime or not')
n = int(input('Enter Number:- '))
flag = False
if n == 1 or n == 0:
    print(f'Entered number {n} is not prime')
    exit()
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            flag = True
            break
if flag:
    print(f'Entered number {n} is not prime')
else:
    print(f'Entered number {n} is prime')
"""
Enter number to check prime or not
Enter Number:- 11
Entered number 11 is prime
"""
"""
Enter number to check prime or not
Enter Number:- 1
Entered number 1 is not prime
"""
"""
Enter number to check prime or not
Enter Number:- 0
Entered number 0 is not prime
"""
