import sys
import random
import csv

if len(sys.argv) != 2:
    print("usage: python main.py <csv test file>")
    sys.exit()

print("main")
with open(sys.argv[1], 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    i = 0
#    for row in spamreader:
#        print i, ':'
#        print ', '.join(row)
#        i += 1
    for row in reader:
        print (row)
