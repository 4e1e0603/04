# Functions

## Zabudované (builtin) funkce.
# https://docs.python.org/3/library/functions.html

## Vlastní (custom) funkce


def function_name(a: int, b: int) -> int:
    """Dokumentace."""
    return a + b


def function1():
    return "Hello from function 1"


def function2():
    return "Hello from function 2"


fn = lambda n: n + 1


def fun1(fun2, a):
    return fun2(a) + 1


fun1(fun2=lambda x: x + 1, a=10)


fun1 = lambda n1: lambda n2: n1 + n2

func = function1.__code__
func = function2


print(func())


def f():
    ...


print(function_name(1, 2))


def f(a, b, c):
    return a + b + c


def f(lst):
    return lst[0] + lst[1] + lst[3]


def f(*numbers):
    return map(lambda x: x + 1, numbers)


def f(*numbers):
    print(numbers)


def f(**letters):
    return print(letters)


# Funkce je objekt.

print(type(f))

print(f.__doc__)
print(f.__annotations__)

print(dir(f))
print(f.__class__)

# Mind blowing: first class functions


def g(a):
    def h(b):
        return a + b

    return h


def hh(f):
    return f(1)


# print(  g(1)(2) )

# print(hh(lambda x: x + 1))


def f(a, b=1):
    ...


f(a=1)

f(a=1, b=2)

f(1)

f(b=2, a=1)
