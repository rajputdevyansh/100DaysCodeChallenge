# A program to demonstrate all dictionary methods
# clear() method removes all the elements from a dictionary.
d1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
print(d1)
d1.clear()
print(d1)
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2021}
{}
"""

# copy() method returns a copy of the specified dictionary.
d2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
print(d2)
x1 = d2.copy()
print(x1)
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2021}
{'brand': 'Ford', 'model': 'Mustang', 'year': 2021}
"""

# fromkeys() method returns a dictionary with the specified keys and the specified value.
d3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
d4 = 0
x2 = d3.fromkeys(d3, d4)
print(x2)
"""
{'brand': 0, 'model': 0, 'year': 0}
"""

# get() method returns the value of the item with the specified key.
d5 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
x3 = d5.get("model")
print(x3)
"""
Mustang
"""

# items() method returns a view object. key-value pairs of the dictionary, as tuples in a list.
d6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
x4 = d6.items()
print(x4)
"""
dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2021)])
"""

# keys() method returns a view object. The view object contains the keys of the dictionary, as a list.
d7 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
x5 = d7.keys()
print(x5)
"""
dict_keys(['brand', 'model', 'year'])
"""

# pop() method removes the specified item from the dictionary.
d8 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
print(d8)
d8.pop("year")
print(d8)
"""
{'brand': 'Ford', 'model': 'Mustang'}
"""

# popitem() method removes the item that was last inserted into the dictionary.
d9 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
print(d9)
d9.popitem()
print(d9)
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2021}
{'brand': 'Ford', 'model': 'Mustang'}
"""

# setdefault() method returns the value of the item with the specified key.
d10 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
x6 = d10.setdefault("model", "Viggo")
print(x6)
"""
Mustang
"""

# update() method inserts the specified items to the dictionary.
d11 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
print(d11)
d11.update({"model": "Viggo"})
print(d11)
"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 2021}
{'brand': 'Ford', 'model': 'Viggo', 'year': 2021}
"""

# values() method returns a view object. The view object contains the values of the dictionary, as a list.
d12 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 2021
}
x7 = d12.values()
print(x7)
"""
dict_values(['Ford', 'Mustang', 2021])
"""
