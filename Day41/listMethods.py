# A program to demonstrate all list methods
# append() method appends an element to the end of the list.
l1 = ["one", "two", "three"]
print(l1)
l1.append("four")
print(l1)
"""
['one', 'two', 'three']
['one', 'two', 'three', 'four']
"""

# clear() method removes all the elements from a list.
l2 = ["one", "two", "three"]
print(l2)
print(l2.clear())
"""
['one', 'two', 'three']
None
"""

# copy() method returns a copy of the specified list.
l3 = ['one', 'two', 'three', 'four']
x1 = l3.copy()
print(x1)
"""
['one', 'two', 'three', 'four']
"""

# count() method returns the number of elements with the specified value.
l4 = ['one', 'two', 'three']
x2 = l4.count('two')
print(x2)
"""
1
"""

# extend() method adds the specified list elements (or any iterable) to the end of the current list.
l5 = ['one', 'two', 'three']
l6 = ['four', 'five']
l5.extend(l6)
print(l5)
"""
['one', 'two', 'three', 'four', 'five']
"""

# index() method returns the position at the first occurrence of the specified value.
l7 = ['one', 'two', 'three']
x3 = l7.index('one')
print(x3)
"""
0
"""

# insert() method inserts the specified value at the specified position.
l8 = ['one', 'two', 'three']
print(l8)
l8.insert(1, 'four')
print(l8)
"""
['one', 'two', 'three']
['one', 'four', 'two', 'three']
"""

# pop() method removes the element at the specified position.
l9 = ['one', 'two', 'three']
print(l9)
l9.pop(1)
print(l9)
"""
['one', 'three']
"""

# remove() method removes the first occurrence of the element with the specified value.
l10 = ['one', 'two', 'three']
print(l10)
l10.remove("one")
print(l10)
"""
['two', 'three']
"""

# reverse() method reverses the sorting order of the elements.
l11 = ['one', 'two', 'three']
print(l11)
l11.reverse()
print(l11)
"""
['one', 'two', 'three']
['three', 'two', 'one']
"""

# sort() method sorts the list ascending by default.
l12 = ['one', 'two', 'three']
print(l12)
l12.sort()
print(l12)
"""
['one', 'two', 'three']
['one', 'three', 'two']
"""
