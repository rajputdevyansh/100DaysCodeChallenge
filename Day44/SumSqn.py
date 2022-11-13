# gfg practice list(Basic)
# Program for Sum of squares of first n natural numbers
print('Enter number to get Sum of squares of first n natural numbers')
n = int(input('Enter number:- '))
sumi = 0
for i in range(0, n+1):
    sumi = sumi+i**2

print(sumi)
"""
Enter number to get Sum of squares of first n natural numbers
Enter number:- 5
55
"""
