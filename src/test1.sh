#!/bin/bash
python3 main.py ../datasets/keijzer-10-train.csv ../datasets/keijzer-10-test.csv 50 50 0.6 0.3 2 > exp4.log
python3 main.py ../datasets/keijzer-10-train.csv ../datasets/keijzer-10-test.csv 50 50 0.6 0.3 3 > exp5.log
python3 main.py ../datasets/keijzer-10-train.csv ../datasets/keijzer-10-test.csv 50 50 0.6 0.3 4 > exp6.log
python3 main.py ../datasets/keijzer-10-train.csv ../datasets/keijzer-10-test.csv 50 50 0.6 0.3 5 > exp7.log
python3 main.py ../datasets/house-train.csv ../datasets/house-test.csv 50 50 0.6 0.3 4 > ../test-logs/house/tournament/exp2.log
python3 main.py ../datasets/house-train.csv ../datasets/house-test.csv 50 50 0.6 0.3 5 > ../test-logs/house/tournament/exp3.log
#python3 -m py_compile main.py
#chmod 755 ./__pycache__/main.cpython-35.pyc
#./__pycache__/main.cpython-35.pyc ../datasets/house-train.csv ../datasets/house-test.csv 500 2500 0.9 0.05 2
