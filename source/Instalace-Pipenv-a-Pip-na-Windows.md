# Python Instalace Windows 7+

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

## Přidej Pipenv do cesty

    $ dir C:\Users\dlanda\AppData\Local\Programs\Python\Python37\libs\Scripts
    Svazek v jednotce C nemá žádnou jmenovku.
    Sériové číslo svazku je E0CA-089E.

    Výpis adresáře C:\Users\dlanda\AppData\Local\Programs\Python\Python37\libs\Scripts

    31.07.2018  10:45    <DIR>          .
    31.07.2018  10:45    <DIR>          ..
    31.07.2018  10:05           102 804 easy_install-3.7.exe
    31.07.2018  10:05           102 804 easy_install.exe
    02.07.2018  16:54               407 just-script.py
    02.07.2018  16:54            74 752 just.exe
    31.07.2018  10:44           102 793 pewtwo.exe
    31.07.2018  10:45           102 786 pip.exe
    31.07.2018  10:45           102 786 pip3.7.exe
    31.07.2018  10:45           102 786 pip3.exe
    31.07.2018  10:44           102 788 pipenv-resolver.exe
    31.07.2018  10:44           102 777 pipenv.exe
    31.07.2018  09:53           102 788 virtualenv-clone.exe
    31.07.2018  09:53           102 783 virtualenv.exe
               Souborů:     12,   Bajtů:              1 103 054
               Adresářů:     2,   Volných bajtů: 362 414 985 216

    $ pip --version
    pip 18.0 from c:\users\dlanda\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
