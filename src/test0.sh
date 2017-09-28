#!/bin/bash
python3 main.py $1 $2 50 50 0.9 0.05 2 > exp0.log
python3 main.py $1 $2 50 50 0.9 0.1 2 > exp1.log
python3 main.py $1 $2 50 50 0.9 0.15 2 > exp2.log
#python3 -m py_compile main.py
#chmod 755 ./__pycache__/main.cpython-35.pyc
#./__pycache__/main.cpython-35.pyc ../datasets/house-train.csv ../datasets/house-test.csv 500 2500 0.9 0.05 2
