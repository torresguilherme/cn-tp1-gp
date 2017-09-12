import sys
import random
import csv

def main():
    if len(sys.argv) != 2:
        print("usage: python main.py <csv test file>")
        sys.exit()

    print("main")
    csvfile = (sys.argv[1], newline = '')
    reader = csv.reader(csvfile, delimiter=' ', quotechat='|')
    for row in reader.split('\n'):
        print(row)

if __name__ == '__main__':
    main()
