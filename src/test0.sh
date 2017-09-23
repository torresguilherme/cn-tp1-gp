#!/bin/bash
python3 main.py ../datasets/house-train.csv ../datasets/house-test.csv 500 2500 0.3 0.05 2
#python3 -m py_compile main.py
#chmod 755 ./__pycache__/main.cpython-35.pyc
#./__pycache__/main.cpython-35.pyc ../datasets/house-train.csv ../datasets/house-test.csv 500 2500 0.3 0.05 2
