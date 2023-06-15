import sys

import ctypes
import ctypes.wintypes


def show_messagebox(message) -> None:
    
    ctypes.windll.user32.MessageBoxW(
        None, ctypes.wintypes.LPCWSTR(message), u"Windows MesageBox Example", 0)
    sys.exit(0)


if __name__ == "__main__":

    if sys.platform != 'win32':
        sys.stderr("This example runs only under Windows!")
        sys.exit(1)
    
    show_messagebox("Hello world!")