#!/bin/bash
python3 -m py_compile main.py
chmod 755 ./__pycache__/main.cpython-35.pyc
./__pycache__/main.cpython-35.pyc ../datasets/house-train.csv ../datasets/house-test.csv 500
