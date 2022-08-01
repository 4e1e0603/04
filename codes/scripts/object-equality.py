
#

"""
Object equality and identity `__eq__` and `__hash__`.
"""

from __future__ import annotations

from typing import Any, Union, Optional


class Person:
    """
    A domain entity object.
    """

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    def __eq__(self, that: object) -> bool:
        return isinstance(that, type(self)) and (self.id == that.id)

    def __hash__(self) -> int:
        return hash((type(self), self.id))

if __name__ == "__main_":

    print("==============================")

    # Stejné osoby

    p1 = Person(1, "Adam")
    p2 = Person(1, "Adam")

    assert p1 == p2 and p2 == p1

    # Různé osoby ale jmenovci

    q1 = Person(1, "Adam")
    q2 = Person(2, "Adam")

    assert q1 != q2


    r1 = Person(1, "Adam")
    r2 = None

    assert r1 != r2 and r2 != r1