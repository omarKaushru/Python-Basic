""""
#    ‘To understand recursion, you must first understand recursion’
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(4))


# sum of n number using for loop

def sum_f(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum


# sum of n number using recursion technique

def sum_r(n):
    print(n)
    if n == 1:
        return 1
    return n + sum_r(n - 1)


print('Sum of n number using loop', sum_f(5000))
print('Sum of n number using recursion', sum_r(100))



# reversing a list using loop

def reverser_l(list):
    new_list = []
    for i in range(0, len(list)):
        new_list.append(0)
    for i in range(len(list) - 1, -1, -1):
        new_list[len(list) - 1 - i] = list[i]
    return new_list


def reverse_r(list):
    if len(list) == 0:
        return []
    return [list[-1]] + reverse_r(list[:-1])


list = [1, 2, 3, 4, 5]
print(reverser_l(list))
print(reverse_r(list))
"""


def summation(num_list):
    if len(num_list) == 0:
        return 0
    if num_list[-1] % 2 == 0:
        return num_list[-1] + summation(num_list[:-1])
    else:
        return summation(num_list[:-1])


a = summation([1, 2, 3, 4, 6, 10, 11, 121, 1009])

print(a)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


for i in range(0, 5):
    print(fib(i), end=" ")

l = []


def convert_number(num):
    if num == 0:
        return l
    digit = num % 2
    l.append(digit)
    convert_number(2)


convert_number(6)
l.reverse()
for i in l:
    print(i, end=" ")
