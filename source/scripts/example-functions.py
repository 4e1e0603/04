
from typing import Callable


def p() -> None:
    """
    Tato funkce, nebo-li procedura nevrací žádnou hodnotu,
     respektive vrací speciální typ `None`.

     -> `None` za () je nepovinný *type hint*
    """
    print("procedure")


def f1(x, y):
    """
    :param x: description
    :type  x: int
    :param y: description
    :type  y: int
    """
    return x + y


def f2(x: int, y: int) -> int:
    return x + y


def f3(f: Callable):
    """
    *Function* is *first class citizen*.
    :param f: nejaká Funkce    
    """
    x = 1
    y = 1
    return f(x, y)


def create_adder(incr: int):
    def inner(x):
        return x + incr

    return inner

print(f1("a", "b")) 
print(f2("a", "b")) 
print(f2(1, 2)) 

print(f3(f2)) 


add_one = create_adder(1)

print( add_one(1) )
print( add_one(2) )
print( add_one(3) )

print("_______")

add_two = create_adder(2)

print( add_one(1) )
print( add_one(2) )
print( add_one(3) )
