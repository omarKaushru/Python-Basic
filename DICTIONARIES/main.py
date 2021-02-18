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
# print(str(omar.get('Name', 'DEFAULT')))
# print(str(omar.get('Age', 'DEFAULT')))
# the setdefault() method
# The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "White")

print(x)
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)


# This program calculate the character frequencies in a text
import pprint as pp
text = 'A quick brown jumps over the lazy dog. This is a sample text to TEST the code.'
letters = {}
for i in text:
  letters.setdefault(i, 0)
  letters[i] = letters[i] + 1
  # letters[h] = letters[h] + 1

# print(letters)
# print the frequencies in alphabetical order
pp.pprint(letters)

# This program calculate the word frequencies in a text
import pprint as pp

text = 'A quick brown brown over jumps over the lazy dog. This is a sample text to TEST the code.This is a sample text to TEST the code.'

words = text.split()
#print(word)

counts = dict()

for word in words:
  if word in counts:
    counts[word] += 1
  else:
    counts[word] = 1

pp.pprint(counts)
"""