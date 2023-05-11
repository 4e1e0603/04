<div style="font-size:3em">Python installation and setup</div>

_Master your development environment_

## Working on command line

> To be able to fully work with many tools, it is essential to know how to use the terminal.

- Ubuntu: https://ubuntu.com/tutorials/command-line-for-beginners#1-overview
- Windows:  https://docs.microsoft.com/en-us/windows/terminal
- macOS: https://iterm2.com/


## Why operating system matter (sometimes)?

__Because some Python most successfull packages as `numpy` uses compiled libraries under the hood!__
These libraries were written in C, C++ or Fortran and then compiled for specific processor and operating system.
These binary packages cannot be moved to another operating system because the binary format differs for each processor and operating system. The version of compiler of these packages has to match the version of compiler of Python interpretrer. This is quite complicated topic so we will finish here. For more information read https://www.python.org/dev/peps/pep-0384/.


## Python on Windows

For some really weird reason a lot of people are using operating system Windows. If you are that person are the few tips how to survive. There are at least three options how to install and use Python on Windows.

1. Install Python binaries
2. Install Python anaconda
3. Install Python under Windows Subsystem for Linux (WSL)

### Python MSI

Go to page https://www.python.org/downloads/windows/ and choose the version of Python.

> [czech] Na stránce je jsou najdete _stable releases_ pro každou dostupnoy verzi a to ve dvou variantách -- jako 32bit a 64bit.
> Pokud nemáte nějaký zvláštní důvod, např návaznost na nějakou knihovnu kompilovanou též pro 32bit, pak zcela jistě vyberte 64bit např.
> pro stabulní verzi Python 3.9.0 - Oct. 5, 2020 vybereme položku _Download Windows x86-64 executable installer_.

    - python-3.8.6-amd64.exe
    - python-3.9.0-amd64.exe
                 ^--------------+ patch version number
               ^----------------+ minor version number
             ^------------------+ major version number

When Python is installed on the systeme for the first time the lanuncher is added to the `PATH` environment variable. From this moment it is recomended to use this launcher to swithc between Ptyhon version in different projects. More information you can find here https://docs.python.org/3/using/windows.html#python-launcher-for-windows.

> Note: Whe you don't know how to uese any program you can ussually write his name with some flag e.g:

    py --help

The command prints the list of installed Python interpreters.

    py --list

    Installed Pythons found by C:\Windows\py.exe Launcher for Windows
    -3.9-64 *
    -3.8-64
    -3.7-64
    -3.6-64

How we can see there are a few installed Python interpreters on our system. The line marked with a star symbol represents the interpreter which `py.exe` choose as a default.

    py --version
    Python 3.9.0

This version can differ from the version which is present as deafault in the Windows `PATH` variable.

    python --version
    Python 3.7.4

## How to start interpreter from the command line

    py
    Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

    py -3.8


    ls 'C:\Users\dlanda\AppData\Roaming\Python\Python38\'

## Virtual environment

Read this to know what is a virtual environment.

### Create the virtual environment

    py -3.7 -m venv .venv

    C:\Users\username\Projects\Personal> ls

        Directory: C:\Users\username\Projects\Personal

    Mode                LastWriteTime         Length Name
    ----                -------------         ------ ----
    d-----       10/23/2020   9:47 AM                .venv

### Activate the virtual environment

    .\.venv\Scripts\activate

    (.venv) PS C:\Users\username\Projects\Personal>

Now everything will be isntalled inside this environment, see this output of `pip` command.

    (.venv) PS C:\Users\username\Projects\Personal>  pip --version
    pip 19.0.3 from c:\users\username\projects\personal\.venv\lib\site-packages\pip (python 3.7)

## Resources

-
- https://docs.python.org/3/using/windows.html

# Python

Welcome! These are my notes on programming for scientific programming in Python. At the beginning I must warn you if you are new to programming. It is a hard and long way ([Teach Yourself Programming in Ten Years](https://norvig.com/21-days.html)).

# Jupyter

[TODO] What is Jupyter, JupyterLab and IPython?

## Jupyter installation

In ths article we will show how to install and run IPython notebook woth Jupyter. More specifically we  will use JupyterLab. We will use only Python > 3.3!

1. Create the project folder and move inside.

```
$ mkdir myproject
$ cd myproject
```

Now we will use the `venv` which will create the viraul environmetn inside the project folder. The widely used convention is name it `.venv`.

```
$ py -3.7 -m venv .venv
```

Now there is an `.venv` folder and inside it is the script which we will use. Thos script activates the virtual environment. In the other words it creates the symbolic link pointing to the python interpreter located inside the `.venv` folder.

```
.venv\Scripts\activate
```

```
$ python --version
Python 3.7.3
```


# JupyterLab

```
$ pip install jupyter
```

```
jupyter --version                                                                                                                               jupyter core     : 4.6.1
jupyter-notebook : 6.0.2
qtconsole        : not installed
ipython          : 7.10.2
ipykernel        : 5.1.3
jupyter client   : 5.3.4
jupyter lab      : 1.2.4
nbconvert        : 5.6.1
ipywidgets       : not installed
nbformat         : 4.4.0
traitlets        : 4.3.3


# Install Python v3.6 on Ubuntu Linux

https://tecadmin.net/install-python-3-6-ubuntu-linuxmint/

Python 3.6.2 is the latest stable version at time of writing of tutorial. This Python version is available to download and install. This article will help you to install Python 3.6.2 on Ubuntu and Linuxmint operating system. To know more about this version visit Python official website.

## Step 1 – Install Required Packages

Use the following command to install prerequisites for Python before installing it.

    sudo apt-get install build-essential checkinstall
    sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

## Step 2 – Download Python 3.6.2

Download Python using following command from python official site. You can also download latest version in place of specified below.

    cd /usr/src
    sudo wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz

Now extract the downloaded package.

    sudo tar xzf Python-3.6.2.tgz

## Step 3 – Compile Python Source

Now use below set of commands to compile python source code on your system using altinstall.

    cd Python-3.6.2
    sudo ./configure
    sudo make altinstall
    make altinstall is used to prevent replacing the default python binary file /usr/bin/python.

## Step 4 – Check the Python Version

Finally, you have successfully installed Python 3.6 on your system. Let’s check the version installed of python using below command

    python3.6 -V
    Python 3.6.2
