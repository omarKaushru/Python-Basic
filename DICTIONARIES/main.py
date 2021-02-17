""""
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
"""
# Dictionary Methods
omar = {'Name': 'Md Omar Kaushru','Phone': '01712-166516', 'Job': 'Software Engineer'}
"""
# printing values
for i in omar.values():
    print(i)
# printing keys
for i in omar.keys():
    print(i)
# printing both keys and values
for i in omar.items():
    print(i)

"""
# Separating keys and values into the list for the dictionary
# x = list(omar.keys())
# y = list(omar.values())
# print(x)
# print(y)
# another technique
# for x,y in omar.items():
#    print('Key: '+x+' Value: '+y)

# use of in keyword
# print('Name' in omar)
# print('Age' in omar)
# print('Md Omar Kaushru' in omar.values())
# print('Age' in omar.keys())

# the get() method
print(str(omar.get('Name', 'DEFAULT')))
print(str(omar.get('Age', 'DEFAULT')))
