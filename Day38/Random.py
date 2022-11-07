# Create a program to generate random answer to a question

import random
print('Will you come to college today!')
ans = random.randint(1, 3)
if ans == 1:
    print('Yes')
if ans == 2:
    print('No')
if ans == 3:
    print('Maybe')
"""
Output 1:
Will you come to college today!
Maybe
Output 2:
Will you come to college today!
No
Output 3:
Will you come to college today!
Yes
"""
