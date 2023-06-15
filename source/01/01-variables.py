# -*- coding: utf-8 -*-

"""
Examples 01: variables

Víceřáddkový komentář.
První v souboru se použiže pro dokumentaci modulu.
"""

print(__doc__ )

# 1. Variable 

print(1 + 1)

# Binding

average = 1

cat_count: int = 2
print( type(cat_count) )

cat_count: float = 1.0  
print( type(cat_count) )

cat_count: int = 1.0 # lžu  
print( type(cat_count) )

# print( cat_count.__annotations__)

cat_count = 1 #type: int

print(cat_count + average) 

# 2. Constant
# Konvence vše je uppercase

DEMO_CONSTANT: int = 1
DEMO_CONSTANT =  2 # nenene

# Numerické datové typy
print(int)
print(float)

# Textový řetězec.
print(str)

# Pravdivostní (Boolovská) hodnota (bool/boolean)
print(bool)

print(
    isinstance(1, int),
    isinstance(1.0, float),
    isinstance(True, bool)
)