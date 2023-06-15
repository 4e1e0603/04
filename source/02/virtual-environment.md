# Jak začít s Pythonem

## Python Instalace Windows 7+

Nainstalujeme 64-bit verzi Python interpreteru, který stáhneme z webu projektu.
Při instalacu nezapomene vybrat možnost "Add Python to Path".

Z příkazové řádky by nyní měl být dostupný

    $ where python
    C:\Users\{username}\AppData\Local\Programs\Python\Python37\python.exe

    python --version
    Python 3.7.0

Pro instalaci balíčků se používá pip, ale hned na zčátek upozorním, že ho bueme používat jen vyjímčně a místo něho budeme používat nástroj Pipenv.

    python -m pip --version
    pip 18.0 from C:\Users\{username}\AppData\Local\Programs\Python\Python37\lib\site-packages\pip (python 3.7)

    $ python -m pip3 --version
    C:\Users\{username}\AppData\Local\Programs\Python\Python37\python.exe: No module named pip3

## Upgrading pip on

    python -m pip install --upgrade pip


## 2. Použití balíčku `venv` ze standardní knihovny

**Tohle je pořád využívaný, ale již v budoucnu tzv. *old school style*.**

Pro vytvoření virtuálního prostředí nám postačí modul `venv`, který je od verze 3.5 (?) součástí standardní knihovny. Jistě víte, že hodně modulů, kromě toho, že je můžeme použít (importovat) ve vlastním programu, může sloužit také jako klasický konzolový program a to tak, že do kódu přidáme známou sekci `if __name__ == '__main__: ...`. Pokud se nacházíme v adresáři našeho projektu můžeme jednoduše zavolat modul `venv` s parametry a ten nám vytvoří adresář obsahující kopii interpretru a knihoven.


Vytvoříme adresář, který obsahuje jak interpretr, tak standardní knihovnu izolovanou od globální instalace.

    python3.6 -m venv env

Po aktivace, se vše již instaluje do aktuálního virtuální prostředí.

    source env/bin/activate

Nyní můžeme instaloval zvolené knihovny.

    pip install request

Pozor, před každou prací, musíme toto virtuální prostředí aktivovat. Po přemístění adresáře `env` nám nebude virtuální prostředí správně fungovat, protože vše je provázané odkazy. Je lepší ho vytvořit prostě znovu.

### Zamknutí aktuálně instalovaných závislosti

    pip freeze > requirements.txt

### Popis nevýhod tohoto způsobu aneb proč používat `pipenv`


## Tvorba  balíčku lokálně -- použití  v jiných balíčcích.
TODO