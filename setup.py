

from setuptools import setup

setup(
    name="course_python",
    version="0.1.0",
    py_modules=["."],
    install_requires=[
        "mypy",
        "pytest",
        "jupyterlab",
    ]
)