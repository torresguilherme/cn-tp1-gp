#!/bin/bash
python -m py_compile main.py
chmod 755 main.pyc
./main.pyc ../datasets/house-train.csv
