# Examples in Python

![Python](https://img.shields.io/badge/Language-Python-blue.svg)


Examples how to emulate the functional paradigm in Python.

## Install

    pip install .      # production mode
    pip install -e .   # development mode


You can typecheck the module as

    mypy <module_name.py>


# Course overview


## Basics

- package, module and import
- constant and variable: name, type, value (binding)
- named function, anonymous function aka Lambda, scope and closure
- built-in functions: an overview
- decorator

- conditions: `if`, `elif`, `else`
- iterations: `while`, `for`


## Class and Object

- custom types via `class` definition
- regular class vs data class `@dataclass(...)` decorato
- abstratc class and protocol class
- property, instance method, class method, static method
- speacial (magic) methods `__method__`
- mutable vs immutable
- refence (`id(obj)`) vs attribute equality, overloading `__eq__`, `__hash__` and so on
- `Enum` class

## Collections

- `Mutable` vs `Immutable`
- `List` and `Tuple`
- `Dict`, `DefaultDict`
- ...
- Comprehension: list, dict
- iterator, generator aka lazy evaluation, continuation

## Standard Library

An overview of some useful standard library modules.


## Typed and Functional features

- Higher-order functions
- Referential transparency and pure functions
- Function composition (nesting)
- map, filter enumerate, zip
- itertools, functools
- Currying and partial application
- Typing module in depth

### Type annotations

Type annotations also called *type hints* are usually not a mandatory in dynamically typed languages such as Pytho, Ruby etc., but in many cases, they can help you to better understand of source code. Althought we can easily anotate tho code such as this without any problems

```python
def plus(a: int, b: int) -> int:
    return a + b
```

, for an advanced type annotations we have to import a typing module which contains many usefull classes and functions or decorators.

```python
import typing
```

## Resources

- [More Monads in Python](https://medium.com/swlh/more-monads-in-python-178492f482f6)
- [Haskell: The List Monad](https://www.schoolofhaskell.com/school/starting-with-haskell/basics-of-haskell/13-the-list-monad)
- [Mimic the behavior of a class in Python with currying](https://towardsdatascience.com/classes-in-functional-programming-ee48a50b6235)