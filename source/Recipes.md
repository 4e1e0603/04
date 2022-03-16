## Recipes

**Show all files in the given path.**

```python
import os
for (root_folder, subfolders, files) in os.walk("."):
    for file in files:
        print(file)
```

**Replace multiple white-space in a string by one.**

```python
' '.join(mystring.split())
```

```python
re.sub( '\s+', ' ', mystring ).strip()
```

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