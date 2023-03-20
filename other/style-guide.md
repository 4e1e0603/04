# Poznámky k Pythonu + kuchařka


## Jak organizovat projekt obsahující Jupyter notebooks analýzy
???



- Use the typing module whenever it possible.
  https://docs.python.org/3/library/typing.html

- https://medium.com/@hwayne/stupid-python-tricks-abusing-explicit-self-53d46b72e9e0
- https://medium.com/@hwayne/stupid-python-tricks-abusing-explicit-self-53d46b72e9e0

https://github.com/google/yapf
https://packaging.python.org/guides/single-sourcing-package-version/

https://www.geeksforgeeks.org/transpose-matrix-single-line-python/
	#The list of lists
	list_of_lists = [range(4), range(7)]
	flattened_list = []

	#flatten the lis
	for x in list_of_lists:
	    for y in x:
	        flattened_list.append(y)

	        #The list of lists
	list_of_lists = [range(4), range(7)]

	#flatten the lists
	flattened_list = [y for x in list_of_lists for y in x]

	flattenedlist = sum(listof_lists, [])
	import itertools
	flattened_list  = list(itertools.chain(*list_of_lists))


Do you know there is a negative zero float value?
https://hackernoon.com/negative-zero-bbd5fd790af3

blank lines should never precede any docstring, and should only follow a docstring when it is for a class.
https://stackoverflow.com/questions/18914108/python-pep-blank-line-after-function-definition

Není nutné psát extra práyný řádek před koncem víceřídkového docstringu.
https://github.com/PyCQA/pydocstyle/pull/64
https://openstack.nimeyo.com/28010/openstack-dev-hacking-extra-blank-line-multi-line-docstring?start=10

- How to write setup.py
- Do I need requirements.txt?
- Application entry point
- Interractive shell

Tohle se stane kdzž jsou někde relativní importz a tz chceš použít metioud `exec`

	Processing c:\users\dlanda\projects\personal\py_apsg
	    Complete output from command python setup.py egg_info:
	    Traceback (most recent call last):
	      File "<string>", line 1, in <module>
	      File "C:\Users\dlanda\AppData\Local\Temp\pip-req-build-evm_bc53\setup.py", line 26, in <module>
	        exec(f.read(), package)
	      File "<string>", line 4, in <module>
	    KeyError: "'__name__' not in globals"


Difference between extras_require() and install_requires() in setup.py?


- Write examples and shor tutorials to the module documentation string and use some script to extract.
  It can be tested via doctest or exported to jupuyter notebook.


  """
  Contains the vector types and related functions for vector algebra.

  Examples:

  	Create a vector with given elements.

  	>>> v = Vector(1, 2, 3)
  	>>> v
  	'Vector(1, 2, 3)'

  """


## Struktura projektu


Každý projekt má následující strukturu.

 	src/
 		{package_name}/
 			...
 	tests/
 		...
 	setup.py
 	README.md
 	LICENSE.txt


## Import modulů


#### Zamezte používání tzv. *wild* importu.


	from module import *


Přidáme do `__all__` neexistující symbol, který zamezí používání *wild* importu.


	__all__ = ('DO_NOT_WILD_IMPORT')

##### Odkazy

- [http://xion.io/post/code/python-all-wild-imports.html](http://xion.io/post/code/python-all-wild-imports.html)


Poznámka: Pokud chcete zakázat

Possible to use more than one argument on __getitem__?


#### Preferujte import celého modulu namísto jednotlivých tříd.

##### Důvod

protože ty jsou součástí modulu do kterého jsme importovali!

NE
	from module import Class, function

ANO

	import module
	import module as md # Pokud chceme např. zkrátit název.


## timeit


	python -m timeit -s "[ord(x) for x in 'abcdfghi']"



Zjistit všechny definované routy pro danou Flask aplikaci.


o
`__repr__` je povinný, `__str__` volitelný, nikdy ne naopak.
Pokud objekt nemá definován `__str__` použije se `__str__` == `__repr__`

př.

```python
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return "Point({0}, {1})".format(x, y)

	def __str__(self):
		return repr(self)
```


Nepoužívejte volání magických metod ani uvnitř samotné třídy, dokud to není opravdu třeba.

Namísto obj.__str__(), obj.__len__(), obj.__repr__(), použijeme vestavěné funkce:

```python
str(obj)
len(obj)
repr(obj)
```


## Pořadí metod ve třídě

## Použití `__slots__`



## Python Style Guide

Metodám/Funkcím, které odpovídají na otázku Ano/Ne True/False říkáme predikáty.
Pojmenováváme je např. s prefixem `is_`, `has_`, `can_`. V případě funkcí zřejmě musejí
přebírat jeden nebo více argumentů. Pokud je predikát metoda, nemusí přebírat argument, protože může pracovat s proměnnou třídy nebo instance.

př. funkce

    is_male(person) -> bool

př. metody

    Person.is_male()

**Kdy má/může být metoda property?**

- Pokud potřebujeme jen vracet hodnotu a neměnit stav třídy, pak volíme `property.getter`.

    dog.name

- Pokud potřebujeme též měnit stav třídy a stačí nám k tomu jedinná hodnota, oak přidáme `property.setter`

    dog.name = "Daisy"

  Poznámka: Obecně se snažíme po vutvoření neměnit stav objektu a dělám je tzv. *immutable*.

 Pokud je to nějaká akce, která může měnit vnitřní stav tak preferujeme sémantiku volání funkce.

    person.set_addres

 Kdyz k tomu budes omylem pristupovat jako k properte misto metody, tak se to tise evalne na `True` a nevsimnes si toho

    class C:
        def get(self):
            return False

    c = C()

    if c.get():
        print("ERROR")

    if c.get:
        print("ERROR")


https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-1.1/bzwdh01d(v=vs.71)#cpconpropertyusageguidelinesanchor1
https://stackoverflow.com/questions/1374273/when-to-use-properties-instead-of-functions
https://martinfowler.com/bliki/CommandQuerySeparation.html



## Návrh knihovny


Pokud nechceš, aby tvou třídu někdo rozšiřoval, neexportuj jí z modulu a namísto `__init__` vytvoř funcki stejného jména jako třída.


```python
class _Point2:
    def __init__(self, x, y):
        self.coords = (x, y)

def point2():
    return _Point2(x, y)
```