# This program demostrates a mini number guessing game using random number, if-else, while loop
import random
import time
print(f"""Hi!!
Welcome to This Number Guessing Game
Choose numbers between 1 and 100""")
n = int(input("""Enter 1 to Start OR 2 to Exit
Enter your choice:- """))
if n == 1:
    time.sleep(2)
    print("Number Chosen! Start Guessing!")
    g = int(input("Enter your guess?: "))
    c = random.randint(1, 100)
    gc = 1
    while g != c:
        gc += 1
        if g < c:
            g = int(input("Wrong. You need to guess higher. Try Again! :- "))
        else:
            g = int(input("Wrong. You need to guess lower. Try Again! :- "))
    print(f"Congrats! The right answer was {c}"
          f". It took you {gc} guesses.")
else:
    time.sleep(1)
    print("Shutting Down")
    exit()
"""
Output(when user starts the game)
Hi!!
Welcome to the Number Guessing Game
Choose numbers between 1 and 100
Enter 1 to Start OR 2 to close
Enter your choice:- 1
Number Chosen! Start Guessing!
Enter your guess?: 25
Wrong. You need to guess higher. Try Again! :- 14
Wrong. You need to guess higher. Try Again! :- 89
Wrong. You need to guess lower. Try Again! :- 70
Wrong. You need to guess higher. Try Again! :- 75
Wrong. You need to guess higher. Try Again! :- 78
Wrong. You need to guess higher. Try Again! :- 80
Congrats! The right answer was 80. It took you 7 guesses.
"""
"""
Output(When user exits the game)
Hi!!
Welcome to This Number Guessing Game
Choose numbers between 1 and 100
Enter 1 to Start OR 2 to Exit
Enter your choice:- 2
Shutting Down
"""
