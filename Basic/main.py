# Conditional Statements
"""
a = input()
b = input()

if a > b:
    print(a)
    print("hi")
elif a == b:
    print("equal")
else:
    print(b)
    print("habi jabi")
    print("nothing")
print("egg")
"
# while loop
x = 0
while x < 10:
    print(x)
    x = x+1


# for loop

for i in range(11, 20):
    print(i)
for i in range(20, 50, 5):
    print(i)

for i in range(1001, 2001, 202):
     for j in range(-15, -150, -2):
         for k in range(1, 10):
             print(i, j, k)
"""
"""
# function

def f(a,b):
    return a+b;

print(f(12,23))

# keyword arguments
# end
print("Omar", end='')
print("Kaushru")

# sep (separation)
print('a','b','c', sep='.')



# Examples of scopes: global scope

def f():
    global a
    print(a)

a = 10
f()

# Exception handling
def f(y):
    try:
        return 10000/y
    except:
        return 'can not devide by zero'

x = f(0)
print(x)
"""
"""
# list
list = [1, 2, 3]
print(list)
print(list[2])
list = ["Omar", 1712, True]

print(list)

# nested list

list = [[1, 2, 4], ["Md Omar", "01712", 28]]
print(list)
print(list[1][2])

# negative index
list = [1, 2, 3, 4, 5]
# print the last element

print(list[-1])
# print the second last element
print(list[-2])
# sub list and slicing
list = [11, 23, 212, 33, 12, 123, 34]
print(list[0:3])


print(list[0:])

list2 = ['a', 'b', 'c', 'd']

newList = list + list2
print(newList)

x = ['p', 'q', 'r', 's']
newX = x*2
print(newX)

x = ['p', 0, 9]
del x[0]
print(x)
# List Methods
# index Method
placeVisited = ['Pakistan', 'UAE', 'Bahrain', 'Saudi Arabia', 'bk','xl', 'ak']

# print(placeVisited.index('UAE'))

# the append() method

placeVisited.append('USA')
# print(placeVisited)

# the insert() method
placeVisited.insert(3, 'Singapore')
# print(placeVisited)

# the remove() method

placeVisited.remove('USA')
# print(placeVisited)
# the sort method
placeVisited.sort()
print(placeVisited)
placeVisited.sort(key=str.lower)
print(placeVisited)

placeVisited.sort(key=str.lower, reverse=True)
print(placeVisited)
"""

fav_food = []

while True:
    print('Food no:' + str(len(fav_food)+1) + ' Or press ENTER to stop adding to the list')
    food = input()
    if food == '':
        break

    fav_food = fav_food + [food]

if len(fav_food) != 0:
    print('The Lists are')
    for i in range(len(fav_food)):
        print(fav_food[i])
