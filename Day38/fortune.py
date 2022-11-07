# Create a program to generate random output every time
import random
luck = random.randint(1, 100)
fort = random.randint(1, 3)
fort_text = ''
if fort == 1:
    fort_text = 'You will have a great day!'
if fort == 2:
    fort_text = 'Watch Out! This day might not go as planned'
if fort == 3:
    fort_text = 'Great! You will be getting married this year'
print(f'{fort_text} '
      f'Your Lucky Number is: {luck}')
"""
Output 1:
Watch Out! This day might not go as planned Your Lucky Number is: 93
Output 2:
Great! You will be getting married this year Your Lucky Number is: 97
Output 3:
Great! You will be getting married this year Your Lucky Number is: 60
Output 4:
Watch Out! This day might not go as planned Your Lucky Number is: 17
Output 5:
You will have a great day! Your Lucky Number is: 66
"""
