import sys


def msgbox(message):
    if sys.platform == 'win32':
        import ctypes
        from ctypes.wintypes import LPCWSTR
        ctypes.windll.user32.MessageBoxW(
            None, LPCWSTR(message), u"Windows MesageBox Example", 0)

        sys.exit(1)


if __name__ == "__main__":
    msgbox("Hello world!")