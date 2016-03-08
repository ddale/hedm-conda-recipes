#!/bin/bash

export CFLAGS="-I$PREFIX/include -L$PREFIX/lib"

$PYTHON setup.py install --old-and-unmanageable

rm -rf $PREFIX/bin
rm -rf $SP_DIR/__pycache__
