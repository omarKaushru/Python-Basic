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


f()


def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32

    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result


print(temperature(20))


def decorator(original_func):
    print('I am the decorator function')

    def wrapper():
        print(f'Wrapper executed before {original_func.__name__}()')

        if 5 > 3:
            print('It is true')

        return original_func() + 'Extra String'
