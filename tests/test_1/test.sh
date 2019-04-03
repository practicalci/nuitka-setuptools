#!/bin/bash

set -xeu pipefail

mkdir build
cd build
cmake ../package1/subpackage3/swigpkg
make all
cd ..
pwd
pip install .

python main.py
