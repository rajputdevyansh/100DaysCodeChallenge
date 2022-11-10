# A program to demonstrate all set methods
# add() method adds an element to the set.
s1 = {"one", "two", "three"}
print(s1)
s1.add("four")
print(s1)
"""
{'two', 'one', 'three'}
{'two', 'four', 'one', 'three'}
"""

# clear() method removes all elements in a set.
s2 = {"one", "two", "three"}
print(s2)
s2.clear()
print(s2)
"""
{'one', 'three', 'two'}
set()
"""

# copy() method copies the set.
s3 = {"one", "two", "three"}
print(s3)
x1 = s3.copy()
print(x1)
"""
{'three', 'one', 'two'}
{'three', 'one', 'two'}
"""

# difference() method returns a set that contains the difference between two sets.
s4 = {"one", "two", "three"}
s5 = {"google", "microsoft", "one"}
x2 = s4.difference(s5)
print(x2)
"""
{'two', 'three'}
"""

# difference_update() method removes the items that exist in both sets.
s6 = {"one", "two", "three"}
s7 = {"google", "microsoft", "one"}
s6.difference_update(s7)
print(s6)
"""
{'three', 'two'}
"""

# discard() method removes the specified item from the set.
s8 = {"google", "microsoft", "one"}
print(s8)
s8.discard("one")
print(s8)
"""
{'google', 'microsoft'}
"""

# intersection() method returns a set that contains the similarity between two or more sets.
s9 = {"one", "two", "three"}
s10 = {"google", "microsoft", "one"}
x3 = s9.intersection(s10)
print(x3)
"""
{'one'}
"""

# intersection_update() method removes the items that is not present in both sets
s11 = {"one", "two", "three"}
s12 = {"google", "microsoft", "one"}
s11.intersection_update(s12)
print(s11)
"""
{'one'}
"""

# isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
s13 = {"one", "two", "three"}
s14 = {"google", "microsoft", "one"}
x4 = s13.isdisjoint(s14)
print(x4)
"""
False
"""

# issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False.
s15 = {"one", "two", "three"}
s16 = {"google", "microsoft", "one"}
x5 = s15.issubset(s16)
print(x5)
"""
False
"""

# issuperset() method returns True if all items in the original set, otherwise it retuns False.
s17 = {"one", "two", "three"}
s18 = {"google", "microsoft", "one"}
x6 = s17.issuperset(s18)
print(x6)
"""
False
"""

# pop() method removes a random item from the set.
s19 = {"google", "microsoft", "one"}
print(s19)
s19.pop()
print(s19)
"""
{'google', 'one'}
"""

# remove() method removes the specified element from the set.
s20 = {"google", "microsoft", "one"}
print(s20)
s20.remove("google")
print(s20)
"""
{'microsoft', 'one'}
"""

# symmetric_difference() a set that contains all items from both set, but not the items that are present in both sets.
s21 = {"one", "two", "three"}
s22 = {"google", "microsoft", "one"}
x7 = s21.symmetric_difference(s22)
print(x7)
"""
{'google', 'three', 'two', 'microsoft'}
"""

# symmetric_difference_update() set by removing items that are present in both sets, and inserting the other items.
s23 = {"one", "two", "three"}
s24 = {"google", "microsoft", "one"}
x8 = s23.symmetric_difference_update(s24)
print(x8)
"""
None
"""

# union() method returns a set that contains all items from the original set, and all items from the specified set(s)
s25 = {"one", "two", "three"}
s26 = {"google", "microsoft", "one"}
x9 = s25.union(s26)
print(x9)
"""
{'three', 'two', 'google', 'one', 'microsoft'}
"""

# update() method updates the current set, by adding items from another set (or any other iterable).
s27 = {"one", "two", "three"}
s28 = {"google", "microsoft", "one"}
s27.update(s28)
print(s27)
"""
{'microsoft', 'google', 'one', 'two', 'three'}
"""
