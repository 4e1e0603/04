# c16

**Programming in Python from beginner to advanced level.**

![language-Python](https://img.shields.io/badge/language-Python-blue.svg)

The examples, and exercises in Python programming language [^1]. 

[^1]: Originally written for personal needs but may be useful for other people. Python is easy to learn but not as easy as many people think and definitely not easy to master. 

## Prerequisites

See the [document](groundf/course-python/notes/02%20Prerequisites.md).

## Installation

- Clone the repository.

  ```shell
  git clone https://github.com/groundf/cs1p.git
  ```

- Move to the folder.

  ```shell
  cd cs1p
  ```

- Install dependencies.

  ```powershell
  py -m venv .venv
  .\.venv\source\Scripts\activate
  pip install .
  ```

And read the course content.

### Build

- `sphinx-build . _build/html  -W -a -j auto -n --keep-going`
- `sphinx-autobuild . build/html --port 8081`

## Contribution

&hellip;

## References

- <https://www.sphinx-doc.org/>
- <https://myst-parser.readthedocs.io/>
- <https://myst-nb.readthedocs.io/>
- <https://github.com/sphinx-extensions2/sphinx-autodoc2/>
- <https://sphinx-extensions.readthedocs.io/>
- <https://pypi.org/project/sphinx-autobuild/>
