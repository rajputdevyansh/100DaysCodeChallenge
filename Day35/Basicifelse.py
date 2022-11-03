"""
Task:- To take input of name and age then check age and grant entry output 
"""
name = input("Hi, what's your name? ")
age = int(input("How old are you? "))

if (age < 13):
    print("You're too young to register", name)
else:
    print("Feel free to join", name)    
"""
Output
Hi, what's your name? Devyansh
How old are you? 21
Feel free to join Devyansh
"""
