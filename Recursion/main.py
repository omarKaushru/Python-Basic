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
