""""
# open a file
f = open('a.text', 'w')

# print('Name: '+f.name)
# print('Is it closed?: ', f.closed)
# print('Mode: ', f.mode)
f.write('Md Omar Kaushru. ')
f.close()

# appending to a file
f = open('a.text', 'a')
f.write('C is my favourite Programming Language')
f.close()
# r+ functionality
f = open('a.text', 'r+')
# info = f.read()
# print(info)
# printing first 8 character from the file
info = f.read(8)
print(info)
f.close()
"""
