---
authors: David Landa
created: ...
---

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
