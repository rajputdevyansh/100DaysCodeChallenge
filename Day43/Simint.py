# gfg practice list(Basic)
# Program for simple interest
print('Enter values to calculate simple interest')
p = int(input('Enter initial principal balance:- '))
r = int(input('Annual Interest Rate:- '))
t = int(input('Time (in years):- '))
A = (p*r*t)/100
print(f'Simple Interest:- {A}')
total = A+p
print(f'Total Amount:- {total}')
"""
Enter values to calculate simple interest
Enter initial principal balance:- 1500
Annual Interest Rate:- 8
Time (in years):- 2
Simple Interest:- 240.0
Total Amount:- 1740.0
"""
