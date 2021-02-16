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

# CSV File manipulation
import csv
file = open('Machine.csv')
file_reader = csv.reader(file)
# data = list(file_reader)
# print(data[1])
# print(len(data))
for row in file_reader:
    print('Row No: ' + str(file_reader.line_num)+' ' + str(row))

import csv
output_file = open('Machine.csv', 'w')
output_writer = csv.writer(output_file)
output_writer.writerow(['1', '2', '3', '4', '5'])
output_writer.writerow(['11', '22', '33', '44', '55'])
"""
f = open('a.txt','w+')
f.write('This is an extra line')