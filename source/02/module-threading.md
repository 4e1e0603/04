# Concurrency with threading module

Součástí základní knihovny jazyka Python je i modul `threading`, který nám umožňuje pracovat s vlákny. Vlákna umožňuj rozdělit program tak, že části běžcí v ruzných vláknech, mohou běžet souběžně (*concurrently*).

Pokud pouštíme Python program, pak spouštíme vlastně kopii Python interpreteru (`python.exe`) jako jeden samostatný proces operačního systému.
Uvnitř tohoto procesu se náš program spustí v hlavním vlákně (*main thread*).

Toto vlákno je pravě vlákno operačního systému, což má svoje důsledky. Nejde tedy např. o takzvané virtuální (simulovaná) vlákna, jako můžeme najít v jiných jazycích, nazývaná např. *green threads* nebo *fibers* viz <https://en.wikipedia.org/wiki/Green_thread>.


V Pythonu existuje pro vlákna jedno omezení a to, že nemohou běžet paralelně, pouze souběžně!

> Because of Python's Global Interpreter Lock (GIL), the threads within each python process cannot truly run in parallel, unlike threads in other programming languages such as Java, C/C++, and Go. For parallelism you have to create multiple processes, for this python comes with the multiprocessing module.