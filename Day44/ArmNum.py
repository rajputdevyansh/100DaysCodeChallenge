# gfg practice list(Basic)
# Program to check Armstrong Number
print('Enter number to check armstrong')
n = int(input('Enter Number:- '))
temp = n
nl = len(str(n))
s = 0
while n != 0:
    r = n % 10
    s = s+(r**nl)
    n = n//10
if temp == s:
    print(f'The given number {temp} is armstrong')
else:
    print(f'The given number {temp} is not armstrong')
"""
Enter number to check armstrong
Enter Number:- 663
The given number 663 is not armstrong
"""
"""
Enter number to check armstrong
Enter Number:- 153
The given number 153 is armstrong
"""
