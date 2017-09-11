#!/bin/bash
python3 -m py_compile main.py
chmod 755 main.pyc
./main.pyc ../datasets/house-train.csv
