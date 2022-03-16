# Jak začít s Pythonem

## Práce s projektem

[IN-PROGRESS]

Pokud se chystám vytvořit nějaký programový kód, musím si nejdříve položit otázku:

Jde o knihovnu nebo o aplikaci.

V případě že jde o knihovnu, pak uvažujeme o tom, že ji budeme zřejmě používat na více místech, proto je nutné jasně definovat její programové rozhraní. V případě Pythonu tedy na nejvyšší úrovní balíčku v souboru `__init___.py` musíme exportovat všechny proměnné, funkce případně třídy, které chceme nabídnout uživateli k použití. Toto slouží především k rychlé orientaci v balíčku a kontrolu pro vývojáře, nelze tím nahradit dokumentaci, kterou bychom měli taktéž pro veřejné funkce a třídy vytvářet.

## Knihovna

Každá knihovna má minimálně tyto adresáře a soubory:

    {package}/
        {package}/
            __init__.py
        tests/
            test.py
        setup.py

Kde adresář a podadresář `{package}` je názvem knihovny. 

Pro správu virtuálních prostředí a závislostí používám nástroj `pipenv` nikoliv `pip` a textové souboy `requirements.txt` apod.

Přiklad struktury projektu knihovny

Knihovna s jedním hlavním balíčkem a v něm umístěným modulem.

    package/
        __init__.py
        package/
            __init__.py
            module.py

Nejvýše umístěný soubor `__init__.py` jen re-exportuje veřejné funkce a třídy z hlavního balíčku respektive modulu `package/module.py`.  
    
    from .package.module import some_function, SomeClass

Pokud máme složitou adresářovou strukturu, můžeme re-exportovat funkce a třídy i v každém, abychom sami jako vývojáři nemusel psát dlouhé názvy při importu v dalších balíčcích a modulech.
    
    from .packa