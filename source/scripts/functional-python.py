# -*- coding: utf-8 -*-

"""
This script show how to make a function composition and use monads.
"""

from __future__ import annotations # [1] supress warnning when annotation inside class

#
# PART 1
#


# # Kompozice funkcí

# Skládaní funkcí se v matematice označuje jako

# $$
# f \circ g
# $$

# Nejdříve aplikujeme $g$ na $x$ a poté $f$ na výsledek funkce $g$.


"""
This example shows the function composition.
"""

from typing import TypeVar, Protocol, Callable, Generic
from numbers import Number, Integral

T = TypeVar("T")
U = TypeVar("U")
V = TypeVar("V")

# Let `f`, `g`, `h` be a function of numerical variable `x`.


def f(x: int) -> int:
    return x * 2


def g(x: int) -> int:
    return x + 2


def h(x: int) -> str:
    return x ** 2


x: int = 2


print(f"Let x = {x}")

print(f"f(x) = {f(x)}, g(x) = {g(x)}, h(x) = {h(x)}")

print(f"Function composition f ∘ g ∘ h = { f(g(h(x))) }")

print(f"Function composition h ∘ g ∘ f = { h(g(f(x))) }")

# This is the same as this steps where we store the function value in intermediate variable.

v1 = h(x)
v2 = g(v1)
v3 = f(v2)

print(f"v3 = {v3}")


def compose(f1: Callable[[U], V], f2: Callable[[T], U]) -> Callable[[T], V]:
    """
    Return the composition of two functions.
    """
    def output(v: T) -> V:
        return f1(f2(v))
    return output


print(compose(g, h)(x))

print

# f . g . h

print(
    "Functionl composition:",
    f(g(h(x))),
    compose(f, compose(g, h))(x)
)


print("---------------")


class Value(Generic[T]):
    """
    Chain functions as ``value(x) >> f >> g >> print``.
    """

    def __init__(self, value: T) -> None:
        self.value = value

    def __rshift__(self, that) -> Value: # ^[1]
        print(f"{that.__name__}({self.value})")

        return type(self)(that(self.value))

    def __call__(self):
        return self.value


Value(x) >> f >> g >> h >> print


#
# PART 2
#




from abc import ABC, abstractmethod

class Monad(ABC):
    """
    Abstract class for monads.
    """

    @abstractmethod
    def bind(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def unit(self) -> None:
        raise NotImplementedError
