# DICTIONARIES

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(thisdict)
# Print the "brand" value of the dictionary:
# print(thisdict["brand"])

# Duplicates Not Allowed Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
# print(thisdict)

# Dictionary Length
# print(len(thisdict))
# Dictionary Items - Data Types
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["colors"])
print(type(thisdict))

# concatenating two dictionaries
A = {'a': 100,
     'b': 200,
     'c': 300}
B = {'x': 400,
     'y': 500,
     'z': 600}

new_dic = A.copy()
new_dic.update(B)
print(new_dic)