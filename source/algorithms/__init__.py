"""
The project top level module.
"""


__version__ = '0.1.0'
__author__ = 'David Landa'
__author_email__ = 'david.landa@protonmail.com'


from .sorting.quick_sort import quick_sort
from .sorting.bubble_sort import bubble_sort


if __name__ == '__main__':
    
    import doctest
    # Some experiments with doctest
    parser = dt.DocTestParser()

    """
    args = {
        'text'     : self.fspath.read(),
        'filename' : str(self.fspath),
        'name'     : self.fspath.basename,
        'globs'    : {'__name__': '__main__'},
        'lineo'    : 0,
    }
    
    tests = parser.get_doctest(**args)
    print(tests)
    """