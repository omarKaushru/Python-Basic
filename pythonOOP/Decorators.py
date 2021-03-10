""""
def outer(message):
    print('In the outer function')

    def inner():
        print('In the inner function')
        print(message)

    return inner


# f = outer('Hello World')
#  calling the function inside the outer function
# f()

def f():
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()


# f()


def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result


# print(temperature(20))

"""


def decorator(original_func):
    print('I am the decorator function')

    def wrapper():
        print(f'Wrapper executed before {original_func.__name__}()')

        if 5 > 3:
            print('It is true')

        return original_func()

    return wrapper


def decorator_2(original_func):
    print('I am the decorator_2 function')

    def wrapper(*args, **kwargs):
        print(f'Wrapper executed before {original_func.__name__}()')

        if 5 > 3:
            print('It is true')

        return original_func(*args, **kwargs)

    return wrapper


# @decorator
def print_something():
    print('Print_something is being ran!')


# print_something()


@decorator_2
def print_something_more(arg1, arg2):
    print(f'Printing Argument_1 = {arg1} and Argument_2 = {arg2}')


print_something_more(123, 2345)

# using decorator in one way
# decorator_f = decorator(print_something)
# decorator_f()
