"""
Program to demostrate all string methods
"""
# capitalize method returns a string where the first character is upper case, and the rest is lower case.
s = "hello! What A Beautiful Day"
x = s.capitalize()
print(x)
s1 = "hello python!"
x1 = s1.capitalize()
print(s1)
"""
Output
Hello! what a beautiful day
Hello python!
"""

# casefold() method returns a string where all the characters are lower case.
s2 = "HELLO INDIA"
x2 = s2.casefold()
print(x2)
s3 = "hello! What A Beautiful Day"
x3 = s3.casefold()
print(x3)
"""
Output
hello india
hello! what a beautiful day
"""
# center() method will center align the string, using a specified character (space is default) as the fill character.
s4 = "evergreen"
x4 = s4.center(20, "A")
print(x4)
"""
Output
AAAAAevergreenAAAAAA
"""

# count() method returns the number of times a specified value appears in the string.
s5 = "This day, is a very great day!"
x5 = s5.count("day")
print(x5)
"""
Output
2
"""

# encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
s6 = "My name is Råm"
x6 = s6.encode()
print(x6)
"""
Output
b'My name is R\xc3\xa5m'
"""

# endswith() method returns True if the string ends with the specified value, otherwise False.
s7 = "Hello, have a great day."
x7 = s7.endswith(".")
print(x7)
"""
Output
True
"""

# expandtabs() method sets the tab size to the specified number of whitespaces.
s8 = "H\te\tl\tl\to"
x8 = s8.expandtabs(2)
print(x8)
"""
Output
H e l l o
"""

# find() method finds the first occurrence of the specified value.
s9 = "Hello, welcome to India"
x9 = s9.find("welcome")
print(x9)
"""
Output
7
"""

# format() method formats the specified value(s) and insert them inside the string's placeholder.
s10 = "Total {p} rupees"
print(s10.format(p=49))
"""
Output
Total 49 rupees
"""

# index() method finds the first occurrence of the specified value.
s11 = "Hello, welcome to Spain."
x11 = s11.index("to")
print(x11)
"""
Output
15
"""

# isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
s12 = "Devyansh22"
x12 = s12.isalnum()
print(x12)
"""
Output
True
"""

# isalpha() method returns True if all the characters are alphabet letters (a-z).
s13 = "SshivaX"
x13 = s13.isalpha()
print(x13)
"""
Output
True
"""

# isdecimal() method returns True if all the characters are decimals (0-9). This method is used on unicode objects.
s14 = "\u0033"
x14 = s14.isdecimal()
print(x14)
"""
Output
True
"""

# isdigit() method returns True if all the characters are digits, otherwise False.
s15 = "50200"
x15 = s15.isdigit()
print(x15)
"""
Output
True
"""

# isidentifier() method returns True if the string is a valid identifier, otherwise False.
s16 = "Demo"
x16 = s16.isidentifier()
print(x16)
"""
Output
True
"""

# islower() method returns True if all the characters are in lower case, otherwise False.
s17 = "demo"
x17 = s17.islower()
print(x17)
"""
Output
True
"""

# isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
s18 = "741852963"
x18 = s18.isnumeric()
print(x18)
"""
Output
True
"""

# isprintable() method returns True if all the characters are printable, otherwise False.
s19 = "Hello! Are you #1?"
x19 = s19.isprintable()
print(x19)
"""
Output
True
"""

# isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
s20 = "  "
x20 = s20.isspace()
print(x20)
"""
Output
True
"""

# istitle() method returns True if all words a upper case letter, AND the rest are lower case letters, otherwise False.
s21 = "Hello, And Welcome To My World!"
x21 = s21.istitle()
print(x21)
"""
Output
True
"""

# isupper() method returns True if all the characters are in upper case, otherwise False.
s22 = "THIS IS"
x22 = s22.isupper()
print(x22)
"""
Output
True
"""

# join() method takes all items in an iterable and joins them into one string.
s23 = ("John", "Peter", "Vicky")
x23 = "#".join(s23)
print(x23)
"""
Output
John#Peter#Vicky
"""

# ljust() method will left align the string, using a specified character (space is default) as the fill character.
s24 = "banana"
x24 = s24.ljust(10)
print(x24, "is my favorite fruit.")
"""
Output
banana     is my favorite fruit.
"""

# lower() method returns a string where all characters are lower case.
s25 = "Hello my FRIENDS"
x25 = s25.lower()
print(x25)
"""
Output
hello my friends
"""

# lstrip() method removes any leading characters (space is the default leading character to remove)
s26 = "     banana     "
x26 = s26.lstrip()
print("of all fruits", x26, "is my favorite")
"""
Output
of all fruits banana      is my favorite
"""

# maketrans() method returns a mapping table that can be used with the ace specified characters.
s27 = "Hello Ram!"
x27 = s27.maketrans("R", "P")
print(s27.translate(x27))
"""
Output
Hello Pam!
"""

# partition() method searches for a specified string, and splits the string into a tuple containing three elements.
s28 = "I could eat apple all day"
x28 = s28.partition("apple")
print(x28)
"""
Output
('I could eat ', 'apple', ' all day')
"""

# replace() method replaces a specified phrase with another specified phrase.
s29 = "I could eat apple all day"
x29 = s29.replace("apple", "bananas")
print(x29)
"""
Output
I could eat bananas all day
"""

# rfind() method finds the last occurrence of the specified value.
s30 = "I could eat apple all day"
x30 = s30.rfind("apple")
print(x30)
"""
Output
12
"""

# rindex() method finds the last occurrence of the specified value.
s31 = "I could eat apple all day"
x31 = s31.rindex("apple")
print(x31)
"""
Output
12
"""

# rjust() method will right align the string, using a specified character (space is default) as the fill character.
s32 = "apple"
x32 = s32.rjust(10)
print(x32, "is my favorite fruit.")
"""
Output
     apple is my favorite fruit.
"""

# rpartition() method searches for the last occurrence of a string, and splits the string into three elements.
s33 = "I could eat bananas all day, bananas are my favorite fruit"
x33 = s33.rpartition("bananas")
print(x33)
"""
Output
('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
"""

# rsplit() method splits a string into a list, starting from the right.
s34 = "apple, banana, cherry"
x34 = s34.rsplit(", ")
print(x34)
"""
Output
['apple', 'banana', 'cherry']
"""

# rstrip() method removes any trailing characters, space is the default trailing character to remove.
s35 = "     banana     "
x35 = s35.rstrip()
print("of all fruits", x35, "is my favorite")
"""
Output
of all fruits      banana is my favorite
"""

# split() method splits a string into a list.
s36 = "welcome to the jungle"
x36 = s36.split()
print(x36)
"""
Output
['welcome', 'to', 'the', 'jungle']
"""

# splitlines() method splits a string into a list. The splitting is done at line breaks.
s37 = "Thank you for the music\nWelcome to the jungle"
x37 = s37.splitlines()
print(x37)
"""
Output
['Thank you for the music', 'Welcome to the jungle']
"""

# startswith() method returns True if the string starts with the specified value, otherwise False.
s38 = "Hello, welcome to my world."
x38 = s38.startswith("Hello")
print(x38)
"""
Output
True
"""

# strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters
s39 = "     banana     "
x39 = s39.strip()
print("of all fruits", x39, "is my favorite")
"""
Output
of all fruits banana is my favorite
"""

# swapcase() method returns a string where all the upper case letters are lower case and vice versa.
s40 = "Hello My Name Is PETER"
x40 = s40.swapcase()
print(x40)
"""
Output
hELLO mY nAME iS peter
"""

# title() method returns a string where the first character in every word is upper case. Like a header, or a title.
s41 = "Welcome to my world"
x41 = s41.title()
print(x41)
"""
Output
Welcome To My World
"""

# translate() method returns a string where some are replaced with the character described in a dictionary.
# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
s42 = {83:  80}
x42 = "Hello Sam!"
print(x42.translate(s42))
"""
Output
Hello Pam!
"""

# upper() method returns a string where all characters are in upper case.
s43 = "hello spain"
x43 = s43.upper()
print(x43)
"""
Output
HELLO SPAIN
"""

# zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.
s44 = "40"
x44 = s44.zfill(10)
print(x44)
"""
Output
0000000040
"""
