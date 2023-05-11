# -*- coding: utf-8 -*-


"""
The stack data structure implementation.

"""


from typing import Any, Protocol, Generic, Iterable, TypeVar, Optional, List


T = TypeVar("T")


class StackLike(Protocol[T]):
    def pop(self):
        ...

    def push(self, value: T) -> None:
        ...

    def peek(self):
         ...

    # # ---

    # def clear(self):
    #     ...

    # def empty(self):
    #     ...

    # def search(self):
    #     ...


class Stack(Generic[T]):  # dataclass ?
    def __init__(self, values: Optional[Iterable[T]] = None) -> None:
        self._values = [] if values is None else list(values)

    def pop(self) -> None:
        del self._values[-1]
        # or self._values.pop(-1)

    def push(self, value: T) -> None:
        self._values.append(value)
        # or self._value = [value]  + self._value


# ### TESTS ### #


def test_that_empty_stack_is_created() -> None:
    stack: Stack[int] = Stack()

    expects: List[int] = []
    current = stack._values

    assert expects == current


def test_that_fulfilled_stack_is_created() -> None:
    stack = Stack([1, 2, 3])

    expects = [1, 2, 3]
    current = stack._values

    assert expects == current


def test_push_to_empty_stack() -> None:
    stack: Stack[int] = Stack()
    stack.push(1)

    expects = [1]
    current = stack._values

    assert expects == current


def test_push_to_filled_stack() -> None:
    stack = Stack([1, 2, 3])

    stack.push(4)

    expects = [1, 2, 3, 4]  # <-- TOP

    current = stack._values

    assert expects == current


if __name__ == "__main__":
    print(__doc__)
