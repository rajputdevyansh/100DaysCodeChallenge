#create a parametarized fuction
def wash_car(amount):
    if (amount == 12):
        print("Wash with tri-color foam")
        print("Rinse twice")
        print("Dry with large blow dryer")

    if (amount == 6):
        print("Wash with white foam")
        print("Rinse once")
        print("Air dry")

wash_car(12)

"""
Output:- 6
Wash with white foam
Rinse once
Air dry

Output:- 12
Wash with tri-color foam
Rinse twice
Dry with large blow dryer
"""
