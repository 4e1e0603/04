# -*- coding: utf-8 -*-


"""
Shows the usage of
`enumerate()`, *Generator[]*, iterative vs recursive, memoization
`in` operator, `if` statement

See https://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence
"""


from typing import Generator


def fibonacci_num(n: int) -> int:
    """Compute the n-th Fibonacci's number."""
    if n < 2:
        return n
    a, b = 0, 1
    while a <= n:
        a, b = b, a + b
    return b


def fibonacci_seq(n: int) -> Generator[int, None, None]:
    """Compute the Fibonacci's sequence."""
    a, b = 0, 1
    while a <= n:
        a, b = b, a + b
        yield a

def F0(n):
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        yield a

def F1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return F1(n - 1) + F1(n - 2)


def F1b(n):
    if n == 0 or n == 1:
        return n
    return F1b(n - 1) + F1b(n - 2)


def F(n):
    return n if n < 2 else F(n - 1) + F(n - 2)


def F(n):
    return n if n in {0, 1} else F(n - 1) + F(n - 2)


def F3(n):
    if n in (0, 1): return n
    return F3(n - 1) + F3(n - 2)


def F2(n):
    match n:
        case 0: return 0
        case 1: return 1
        case _: return F2(n - 1) + F2(n - 2)


def F4(n):
    match n:
        case 0 | 1: return n
        case _: return F4(n - 1) + F4(n - 2)


if __name__ == "__main__":

    N = 10

    # print(fibonacci_num.__doc__, fibonacci_num.__annotations__)

    for n in range(0, N):
        # print(f"fib({n}) = {fibonacci_num(n)}")
        print(F1(n), F2(n), F3(n), F4(n), F(n))

    print(
        tuple(F0(N))
    )

    print('-' * 10)
    # print(fibonacci_seq.__doc__, fibonacci_num.__annotations__)

    # for i, n in enumerate(fibonacci_seq(N)):
        # print(f"fib({i}) = {n}")
