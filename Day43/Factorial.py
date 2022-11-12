# gfg practice list(Basic)
# Program for factorial of a number
print('Enter number to get factorial')
n = int(input('Enter number:- '))
fact = 1
if n > 0:
    for i in range(1, n + 1):
        fact = fact*i
else:
    print("Enter another number")
    exit()
print(fact)
"""
Enter number to get factorial
Enter number:- 5
120
"""
"""
Enter number to get factorial
Enter number:- 0
Enter another number
"""
