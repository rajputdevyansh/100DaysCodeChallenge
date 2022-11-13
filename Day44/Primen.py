# gfg practice list(Basic)
# program to print all Prime numbers in an Interval
print('Enter number to check prime or not')
x = int(input('Enter Start Point:- '))
y = int(input('Enter End Point:- '))
print(f'Prime numbers between {x} and {y} are:- ')
for i in range(x, y+1):
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
"""
Enter number to check prime or not
Enter Start Point:- 2
Enter End Point:- 7
Prime numbers between 2 and 7 are:- 
2
3
5
7
"""
