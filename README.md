# LSM6DS3 Python Library

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/lsm6ds3-python/test.yml?branch=main)](https://github.com/pimoroni/lsm6ds3-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/lsm6ds3-python/badge.svg?branch=main)](https://coveralls.io/github/pimoroni/lsm6ds3-python?branch=main)
[![PyPi Package](https://img.shields.io/pypi/v/lsm6ds3.svg)](https://pypi.org/project/lsm6ds3/)
[![Python Versions](https://img.shields.io/pypi/pyversions/lsm6ds3.svg)](https://pypi.python.org/pypi/lsm6ds3)

Generated from [the Pimoroni Python Boilerplate](https://github.com/pimoroni/boilerplate-python).

The LSM6DS3TR-C is an always-on 3D accelerometer and 3D gyroscope that includes additional built-in functions such as:

* Pedometer
* Tap and double tap recognition
* Significant motion and tilt detection
* Free-fall detection

# Installing

We'd recommend using this library with Raspberry Pi OS Bookworm or later. It requires Python ≥3.7.

## Full install (recommended):

We've created an easy installation script that will install all pre-requisites and get you up and running with minimal efforts. To run it, fire up Terminal which you'll find in Menu -> Accessories -> Terminal
on your Raspberry Pi desktop, as illustrated below:

![Finding the terminal](http://get.pimoroni.com/resources/github-repo-terminal.png)

In the new terminal window type the commands exactly as it appears below (check for typos) and follow the on-screen instructions:

```bash
git clone https://github.com/pimoroni/lsm6ds3-python
cd lsm6ds3-python
./install.sh
```

**Note** Libraries will be installed in the "pimoroni" virtual environment, you will need to activate it to run examples:

```
source ~/.virtualenvs/pimoroni/bin/activate
```

## Development:

If you want to contribute, or like living on the edge of your seat by having the latest code, you can install the development version like so:

```bash
git clone https://github.com/pimoroni/lsm6ds3-python
cd lsm6ds3-python
./install.sh --unstable
```

## Install stable library from PyPi and configure manually

* Set up a virtual environment: `python3 -m venv --system-site-packages $HOME/.virtualenvs/pimoroni`
* Switch to the virtual environment: `source ~/.virtualenvs/pimoroni/bin/activate`
* Install the library: `pip install lsm6ds3`

In some cases you may need to us `sudo` or install pip with: `sudo apt install python3-pip`.

This will not make any configuration changes, so you may also need to enable:

* i2c: `sudo raspi-config nonint do_i2c 0`


You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.
