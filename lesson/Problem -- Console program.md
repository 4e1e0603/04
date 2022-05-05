Naším prvním úkolem bude napsat konzolový program který načte a zpracuje textový soubor. Tento program bude typu "fire-and-forget", tedy po spuštění provede daný úkol a ihned skončí. Podobně pracují unixově programy jako `cd, ls`, ale i nám známý interpret Pythonu. 

    python my_program.py

Předchozí příkaz samozřejmě spouští náš program zapsaný v `my_program.py`, zaárověň je to krásná ukázka volání interpreteru jako konzolového programu. 

Program se bude instruovat přes tzv. přepínače (*flags*). Takovým přepínačem je např. `-h` respektive `--help` pro vypsání nápovědy o programu.

Poznámka k přepínačům: Ty se podle konvence mohou obvykle zadávat v krátké a dlouhé formě a nápovědě pro přepínač je napsánao např. `-h | --help`, kde svislítko znamená *nebo*. Všimněte si, že v případě krátké formy předchází `-` a v případě dlouhé formy `--`. Pokud krátkaá forma koliduje s jným přepínačem, pak se obvykle zadává jako velké písmeno např. `python --version` ale `python -V`, protože `python -v` se používá pro spuštění interpreteru v tzv *verbose* módu.  