# DataFrames via various languages and libraries

## Motivation

Compare the various `DataFrame` libraries at least well known R (native) and Python (`pandas` package) implementations with
some newer and maybe faster and safer alternatives such as Rust `polar` package, Scala (`spark` package) and Julia (`DataFrames` package).

## Installation

### Python

Unix

    python -m venv .venv
    source .venv/bin/activate

Windows

    py -m venv .venv
    .venv/Scripts/Activate

When the environment is properly acitaved you should see something like

    (venv) ...

and the you can install dependencies

    pip install -r requirements.txt

## Run

    python <script-name.py>