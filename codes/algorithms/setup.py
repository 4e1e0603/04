from setuptools import setup


"""
Learn the algorithms in a simple way.
"""


__package__ = "algos"


def get_readme():
    with open("README.md", encoding="utf8") as f:
        return f.read()


def get_license():
    with open("LICENSE", encoding="utf8") as f:
        return f.read()


def get_version():
    pass
    

exec(open(__package__ + "/__init__.py").read())


setup(
    name=__package__,
    cmdclass='',
    version=__version__,
    license=get_license(),
    description=__doc__,
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    author=__author__,
    author_email=__author_email__,
    url="https://github.com/uetoyo/algos",
    packages=[__package__],
    install_requires=[],
    entry_point='',
    setup_requires=[],
    tests_require=[],
    classifiers=[],
)
