# -*- coding: utf-8 -*-


__all__ = tuple(["hello"])


def hello(name: str) -> str:
    """Returns the greet sentence.

    :param name: The name of the person we want to greet.
    :returns: The greet sentence.
    """
    return f"Hello {name}!"


if __name__ == "__main__":
    print("Hello world")
