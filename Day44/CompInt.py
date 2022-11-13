# gfg practice list(Basic)
# Program for compound interest
print("Enter values to calculate Compound Interest")
p = float(input('Enter Principal amount:- '))
r = float(input('Enter rate:- '))
t = int(input('Enter time span is years:- '))
a = p*(1+r/100)**t
CI = a-p
print(f'Total Amount:- {a}\n'
      f'Compound Interest:- {CI}')
"""
Enter values to calculate Compound Interest
Enter Principal amount:- 15740
Enter rate:- 8.9
Enter time span is years:- 3
Total Amount:- 20327.70583206
Compound Interest:- 4587.705832060001
"""
